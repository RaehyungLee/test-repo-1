# test-repo-1

A small demo app that depends on `test-repo-2` (a cross-repo dependency).

## Dependencies

- `test-repo-2` — sibling repo, pulled in via git.
- `lodash` — pinned to an old version on purpose (dependency scanner test).

## Run

```bash
npm install
npm start
```
