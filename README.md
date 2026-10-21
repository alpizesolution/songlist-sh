# SongHub Songlist

A fast, installable (PWA) songlist for SongHub's 47,998 karaoke songs. Browse titles A–Z, browse by singer, or search by title, singer or song number. Tap a song number to copy it. Works offline after the first visit.

It is a plain static site: no build step is needed to deploy.

## Updating the song list

1. Replace `data/songlist.csv` (columns: `NUMBER,TITLE,ARTIST,...`).
2. Rebuild the data file:

   ```sh
   python3 scripts/build-data.py data/songlist.csv songs.js
   ```

3. Bump `VERSION` in `sw.js` so installed apps fetch the new list.
4. Commit and push. Vercel redeploys automatically.

## Running locally

```sh
python3 -m http.server 8000
```

Then open http://localhost:8000.
