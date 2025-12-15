# Modulo 004 - Git & GitHub
## Comandos essenciais

Este documento descreve os principais comandos executado no git

---

## 1. Clone

Este comando server para você clonar/baixar o reposítorio criado no GitHub para o seu computador. Execute o comando abaixo e troque pela url do seu repositório:
```bash
git clone git@github.com:adminzuplae/aulas_python_dez2025.git
```

## 2. Git Add

Este comando serve para adicionarmos novos arquivos ou arquivos modificados em uma versão.
Execute o comando a seguir para adicionar todos os arquivos novos e modificados:
```bash
git add .
```

Ou para adicionar um arquivo específico:
```bash
git add README.md
```

Ou ainda, para adicionar uma pasta específica:
```bash
git add modulo002/
```

## 3. Git Reset

Este comando é o contrario do Add, serve para tirar arquivos novos e modificações antes de gerar a versão/commit.

Para retirar todos os arquivos novos e modificados:
```bash
git reset .
```

Para remover um arquivo específico:
```bash
git reset README.md
```

Ou ainda, para remover uma pasta específica:
```bash
git reset modulo002/
```
## 4. Git Commit

Este comando serve para gerarmos uma mensagem e associa-la aos arquivos adicionados com o comando **git add**. Execute o comando abaixo trocando a mensagem por uma que faça sentido para suas alterações:

```bash
git commit -m "adicionando arquivos do modulo 002"
```

## 5. Git Push

Este comando serve para mandar para o GitHub todos os commits gerados nesta maquina.

```bash
git push
```

## 6. Git Branch

Este comando serve para verificarmos as branchs que temos neste repositório e tambem para criar uma nova Branch.

Para verificar as branchs existentes execute o seguinte comando:

```bash
git branch
```

Para criar uma nova branch, execute:
```bash
git branch nome_da_nova_branch
```

## 6. Git Checkout

Este comando serve para alternarmos entre branchs.

Execute o comando a seguir para mudar para uma branch criada
```bash
git checkout nome_da_nova_branch
```

Execute o comando a seguir para mudar para a branch principal:
```bash
git checkout main
```

## 7. Atualizando a nova branch no GitHub

Quando você cria uma nova branch com o comando **git branch** você cria ela apenas no seu computador, para atualizar no GitHub você deve executar o comando push da seguinte forma:

```bash
git push -u origin nome_da_nova_branch
```

## 8. Merge

Serve para trazer todos os commits de uma branch para outra. Por exemplo aqui estamos dentro da branch main e estamos trazendo as alterações da nova branch:
```bash
git merge nome_da_nova_branch
```

