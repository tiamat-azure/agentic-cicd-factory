import { defineCollection, z } from 'astro:content';
import { docsSchema } from '@astrojs/starlight/schema';
import { chapitresLoader } from './loaders/chapitres';

export const collections = {
  docs: defineCollection({
    loader: chapitresLoader(),
    schema: docsSchema({
      extend: z.object({
        /** Numéro du chapitre sur 2 chiffres, ex. "01". */
        chapitre: z.string().optional(),
        /** Livrable cumulatif du chapitre, ex. "Agent v0.1". */
        livrable: z.string().optional(),
        livrableDescription: z.string().optional(),
        /** Durée estimée telle que déclarée dans le README du chapitre. */
        duree: z.string().optional(),
        /** Gate du parcours atteint par ce chapitre. */
        gate: z.object({ numero: z.number(), libelle: z.string() }).optional(),
        /** Page issue de `solutions/` : contenu replié par défaut. */
        solution: z.boolean().optional(),
        /** Page issue d’un fichier de code source. */
        code: z.boolean().optional(),
        /** Chapitre pas encore rédigé. */
        aVenir: z.boolean().optional(),
      }),
    }),
  }),
};
