```typescript
import { export1, export2 } from "module-name";
```

## [AST](#AST) 結構

- `ImportDeclaration`
  - `ImportClause`
    - `NamedImports`
      - `ImportSpecifier`
        - `Identifier`
      - `ImportSpecifier`
        - `Identifier`
  - `StringLiteral`