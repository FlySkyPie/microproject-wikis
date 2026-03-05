import fs from 'fs-extra';
import path from 'node:path';

/**
 * Return path of folders under `wikis/` exclude `template`.
 */
export const readWikis = async (): Promise<string[]> => {
  const wikisDir = path.resolve(__dirname, "../../", 'wikis');
  const entries = await fs.readdir(wikisDir, { withFileTypes: true });

  return entries
    .filter(entry => entry.isDirectory() && entry.name !== 'template')
    .map(entry => `${wikisDir}/${entry.name}`);
}

export const copyBuilds = async (wikiFolders: string[]) => {
  const targetFolder = path.resolve(__dirname, "../../", 'dist');
  await fs.ensureDir(targetFolder);
  for (let index = 0; index < wikiFolders.length; index++) {
    const wikiFolder = wikiFolders[index];
    const wikiName = path.basename(wikiFolder);
    const wikiFile = path.resolve(wikiFolder, "output", 'index.html');

    const targetPath = path.resolve(targetFolder, `${wikiName}.html`);

    fs.copyFile(wikiFile, targetPath);
  }
};

const wikis = await readWikis();
await copyBuilds(wikis);
