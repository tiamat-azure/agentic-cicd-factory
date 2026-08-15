// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

/** Les 12 chapitres du parcours, dans l’ordre du fil rouge. */
const CHAPITRES = [
  '01-comprendre-agent',
  '02-tools-function-calling',
  '03-workflows-orchestration',
  '04-mcp',
  '05-llm-agnostic',
  '06-token-engineering-routing',
  '07-observability-tracing',
  '08-evaluation-engineering',
  '09-security-governance',
  '10-agentic-cicd',
  '11-pr-factory',
  '12-production-platform',
];

export default defineConfig({
  site: 'https://tiamat-azure.github.io',
  base: '/agentic-cicd-factory',
  trailingSlash: 'always',
  integrations: [
    starlight({
      title: 'Agentic CI/CD Factory',
      description:
        'Parcours en 12 chapitres pour concevoir, produire et déployer une usine CI/CD nativement agentic.',
      defaultLocale: 'root',
      locales: { root: { label: 'Français', lang: 'fr' } },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/tiamat-azure/agentic-cicd-factory',
        },
      ],
      customCss: ['./src/styles/custom.css'],
      components: {
        PageTitle: './src/components/PageTitle.astro',
        Sidebar: './src/components/Sidebar.astro',
      },
      sidebar: CHAPITRES.map((chapitre) => ({
        label: `${chapitre.slice(0, 2)} · ${libelle(chapitre)}`,
        collapsed: chapitre !== '01-comprendre-agent',
        items: [{ autogenerate: { directory: chapitre } }],
      })),
      editLink: {
        baseUrl: 'https://github.com/tiamat-azure/agentic-cicd-factory/edit/main/',
      },
      lastUpdated: true,
      pagination: true,
    }),
  ],
});

/** `01-comprendre-agent` -> `Comprendre agent`. */
function libelle(chapitre) {
  const mots = chapitre.slice(3).replace(/-/g, ' ');
  return mots.charAt(0).toUpperCase() + mots.slice(1);
}
