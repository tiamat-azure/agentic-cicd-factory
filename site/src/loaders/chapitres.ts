import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative, posix } from 'node:path';
import { fileURLToPath } from 'node:url';
import type { Loader, LoaderContext } from 'astro/loaders';

/**
 * Loader Astro qui expose le contenu des chapitres (`NN-titre/`) situés à la
 * racine du dépôt, SANS le dupliquer dans `site/`. Le markdown des chapitres
 * reste la seule source de vérité.
 */

const RACINE = fileURLToPath(new URL('../../../', import.meta.url));

/** Extensions rendues comme pages. */
const MARKDOWN = new Set(['.md', '.mdx']);
const CODE: Record<string, string> = {
  '.py': 'python',
  '.toml': 'toml',
  '.sh': 'bash',
};

/** Dossiers jamais publiés. */
const IGNORES = new Set([
  'node_modules',
  '.venv',
  '.git',
  '__pycache__',
  '.pytest_cache',
  '.ruff_cache',
  'site',
  '.lavish',
]);

/** Les 5 gates du parcours (voir `ressources/prd/01-PRD.md`). */
const GATES: Array<{ numero: number; chapitres: string[]; libelle: string }> = [
  { numero: 1, chapitres: ['01', '02'], libelle: 'agent sans framework' },
  { numero: 2, chapitres: ['03', '04'], libelle: 'workflow multi-agents' },
  { numero: 3, chapitres: ['05'], libelle: 'changer de LLM sans toucher à l’agent' },
  { numero: 4, chapitres: ['06', '07', '08'], libelle: 'preuve par evals' },
  { numero: 5, chapitres: ['11'], libelle: 'PR générée automatiquement' },
];

/** Titres lisibles des sous-sections d’un chapitre. */
const SECTIONS: Record<string, { titre: string; ordre: number }> = {
  slides: { titre: 'Leçons', ordre: 10 },
  demos: { titre: 'Démos', ordre: 20 },
  exercices: { titre: 'Exercices', ordre: 30 },
  solutions: { titre: 'Solutions', ordre: 40 },
};

function estDossierChapitre(nom: string) {
  return /^\d{2}-[a-z0-9-]+$/.test(nom);
}

function numeroChapitre(nom: string) {
  return nom.slice(0, 2);
}

function gateDe(chapitre: string) {
  return GATES.find((g) => g.chapitres.includes(chapitre));
}

/** `03_agent_minimal` / `01-definitions` -> `Agent minimal` / `Definitions`. */
function titreDepuisNom(nom: string) {
  const sansPrefixe = nom.replace(/^\d{2}[-_]/, '').replace(/[-_]/g, ' ');
  return sansPrefixe.charAt(0).toUpperCase() + sansPrefixe.slice(1);
}

function ordreDepuisNom(nom: string) {
  const m = nom.match(/^(\d{2})/);
  return m ? Number(m[1]) : 99;
}

/** Réécrit les liens relatifs du dépôt vers les routes du site. */
function reecrireLiens(markdown: string, dossierDeLEntree: string) {
  return markdown.replace(/\]\(([^)\s]+)(\s+"[^"]*")?\)/g, (tout, cible: string, titre = '') => {
    if (/^(https?:|mailto:|#|\/)/.test(cible)) return tout;
    const [chemin, ancre = ''] = cible.split('#');
    if (!chemin) return tout;
    let resolu = posix.normalize(posix.join(dossierDeLEntree, chemin));
    resolu = resolu.replace(/\.mdx?$/, '').replace(/\/?README$/i, '');
    resolu = resolu.replace(/\/$/, '');
    const url = '/' + resolu + (ancre ? '#' + ancre : '');
    return `](${url}${titre})`;
  });
}

/** Récupère le premier titre H1 et le retire du corps. */
function extraireTitre(markdown: string): { titre?: string; corps: string } {
  const m = markdown.match(/^#\s+(.+)$/m);
  if (!m) return { corps: markdown };
  return { titre: m[1].trim(), corps: markdown.replace(m[0], '').trimStart() };
}

/** Récupère `> Livrable : **Agent v0.1** - ...` et le retire du corps. */
function extraireLivrable(markdown: string): { livrable?: string; description?: string; corps: string } {
  const m = markdown.match(/^>\s*Livrable\s*:\s*\*\*(.+?)\*\*\s*[-–]?\s*([\s\S]*?)(?=\n\n)/m);
  if (!m) return { corps: markdown };
  const description = m[2]
    .split('\n')
    .map((l) => l.replace(/^>\s?/, '').trim())
    .join(' ')
    .trim();
  return { livrable: m[1].trim(), description, corps: markdown.replace(m[0], '').trimStart() };
}

function extraireDuree(markdown: string) {
  return markdown.match(/Durée estimée\s*:\s*\*\*(.+?)\*\*/)?.[1];
}

async function listerFichiers(dossier: string): Promise<string[]> {
  const entrees = await readdir(dossier, { withFileTypes: true });
  const fichiers: string[] = [];
  for (const e of entrees) {
    if (e.name.startsWith('.') || IGNORES.has(e.name)) continue;
    const chemin = join(dossier, e.name);
    if (e.isDirectory()) fichiers.push(...(await listerFichiers(chemin)));
    else fichiers.push(chemin);
  }
  return fichiers;
}

type Entree = {
  id: string;
  fichier?: string;
  markdown: string;
  data: Record<string, unknown>;
};

async function construireEntrees(): Promise<Entree[]> {
  const entrees: Entree[] = [];

  // --- Page d’accueil : le README racine, source de vérité du sommaire ---
  const readmeRacine = await readFile(join(RACINE, 'README.md'), 'utf8');
  const accueil = extraireTitre(readmeRacine);
  entrees.push({
    id: 'index',
    fichier: join(RACINE, 'README.md'),
    markdown: reecrireLiens(accueil.corps, '.'),
    data: {
      title: accueil.titre ?? 'Agentic CI/CD Factory',
      description: 'Parcours en 12 chapitres pour construire une usine CI/CD nativement agentic.',
      sidebar: { order: 0, label: 'Accueil' },
    },
  });

  const racine = await readdir(RACINE, { withFileTypes: true });
  const chapitres = racine
    .filter((e) => e.isDirectory() && estDossierChapitre(e.name))
    .map((e) => e.name)
    .sort();

  for (const chapitre of chapitres) {
    const numero = numeroChapitre(chapitre);
    const gate = gateDe(numero);
    const fichiers = (await listerFichiers(join(RACINE, chapitre))).filter((f) => {
      const ext = f.slice(f.lastIndexOf('.'));
      return MARKDOWN.has(ext) || ext in CODE;
    });

    const readme = fichiers.find((f) => relative(join(RACINE, chapitre), f).toLowerCase() === 'readme.md');

    // Chapitre pas encore rédigé : page d’attente, pour garder les 12 visibles.
    if (!readme) {
      entrees.push({
        id: `${chapitre}/index`,
        markdown: `Ce chapitre n’est pas encore rédigé.\n\nSeuls les chapitres listés comme « prêt » dans le [sommaire](/) ont un contenu.`,
        data: {
          title: titreDepuisNom(chapitre),
          chapitre: numero,
          aVenir: true,
          sidebar: { order: Number(numero), badge: { text: 'à venir', variant: 'caution' } },
        },
      });
      continue;
    }

    for (const fichier of fichiers) {
      const rel = relative(join(RACINE, chapitre), fichier).split(/[\\/]/).join('/');
      const ext = fichier.slice(fichier.lastIndexOf('.'));
      const brut = await readFile(fichier, 'utf8');
      const estReadmeChapitre = rel.toLowerCase() === 'readme.md';
      const section = rel.includes('/') ? rel.split('/')[0] : undefined;
      const nomFichier = rel.slice(rel.lastIndexOf('/') + 1).replace(/\.[^.]+$/, '');

      let id: string;
      if (estReadmeChapitre) id = `${chapitre}/index`;
      else if (nomFichier.toLowerCase() === 'readme')
        id = `${chapitre}/${rel.slice(0, rel.lastIndexOf('/'))}`;
      else id = `${chapitre}/${rel.replace(/\.[^.]+$/, '')}`;

      let markdown: string;
      let titre: string;
      const data: Record<string, unknown> = { chapitre: numero };

      if (ext in CODE) {
        titre = rel.slice(rel.lastIndexOf('/') + 1);
        markdown = `Fichier \`${rel}\` du chapitre ${numero}.\n\n\`\`\`${CODE[ext]}\n${brut}\n\`\`\``;
        data.code = true;
      } else {
        const t = extraireTitre(brut);
        // « 01 - Comprendre… » : le numéro est déjà porté par la sidebar.
        titre = (t.titre ?? titreDepuisNom(nomFichier)).replace(/^\d{2}(\.\d+)?\s*[-–]\s*/, '');
        markdown = reecrireLiens(t.corps, `${chapitre}/${rel.slice(0, rel.lastIndexOf('/') + 1)}`);
      }

      if (estReadmeChapitre) {
        const l = extraireLivrable(markdown);
        markdown = l.corps;
        if (l.livrable) {
          data.livrable = l.livrable;
          data.livrableDescription = l.description;
        }
        const duree = extraireDuree(markdown);
        if (duree) data.duree = duree;
        if (gate) data.gate = { numero: gate.numero, libelle: gate.libelle };
        data.sidebar = { order: 0, label: 'Vue d’ensemble' };
      } else {
        const meta = section ? SECTIONS[section] : undefined;
        data.sidebar = { order: (meta?.ordre ?? 50) + ordreDepuisNom(nomFichier) };
        if (section === 'solutions') {
          data.solution = true;
          // Le sommaire pointerait vers des titres masqués par le repli.
          data.tableOfContents = false;
        }
      }

      data.title = titre;
      entrees.push({ id, fichier, markdown, data });
    }
  }

  return entrees;
}

async function charger(context: LoaderContext) {
  const { store, parseData, renderMarkdown, logger } = context;
  store.clear();
  const entrees = await construireEntrees();

  for (const entree of entrees) {
    const data = await parseData({ id: entree.id, data: entree.data, filePath: entree.fichier });
    const rendered = await renderMarkdown(entree.markdown);

    // Les solutions restent repliées par défaut (décision produit).
    if (entree.data.solution) {
      rendered.html = `<details class="solution"><summary>🔑 Afficher la solution</summary>${rendered.html}</details>`;
    }

    store.set({
      id: entree.id,
      data,
      body: entree.markdown,
      filePath: entree.fichier ? relative(RACINE, entree.fichier) : undefined,
      rendered,
    });
  }

  logger.info(`${entrees.length} pages chargées depuis les chapitres du dépôt`);
}

export function chapitresLoader(): Loader {
  return {
    name: 'chapitres',
    async load(context: LoaderContext) {
      await charger(context);

      // En dev, recharger dès qu’un fichier de chapitre change.
      context.watcher?.on('all', (_evenement: string, chemin: string) => {
        const rel = relative(RACINE, chemin);
        if (rel.startsWith('site') || rel.startsWith('..')) return;
        if (!/\.(md|mdx|py|toml|sh)$/.test(rel)) return;
        void charger(context);
      });
    },
  };
}
