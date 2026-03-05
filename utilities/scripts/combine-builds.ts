import fs from 'node:fs/promises';

export const readWikis = async (): Promise<string[]> => {
  /**
   * Return path of folders under `wikis/` exclude `template`.
   */
  const wikisDir = 'wikis';
  const entries = await fs.readdir(wikisDir, { withFileTypes: true });
  
  return entries
    .filter(entry => entry.isDirectory() && entry.name !== 'template')
    .map(entry => `${wikisDir}/${entry.name}`);
}
