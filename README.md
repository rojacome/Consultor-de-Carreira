# Consultor de Carreira para Estudantes de Graduação

Um prompt que transforma um agente de IA com busca na web em um consultor de
carreira para estudantes de graduação brasileiros que procuram a primeira
experiência profissional.

Não é um gerador de conselhos genéricos: a consultoria acontece em sete etapas,
com entrevista antes de recomendação, e termina com materiais prontos para uso —
currículo redigido, textos de LinkedIn, estrutura de portfólio e um plano de 30,
60 e 90 dias.

## Comece por aqui

**→ [Abrir o Consultor de Carreira](https://rojacome.github.io/Consultor-de-Carreira/)**

A página tem um formulário com os campos iniciais e um botão que copia o prompt
já preenchido. Você cola no Claude ou no ChatGPT e a conversa começa. Não precisa
entender de GitHub, nem criar conta em nada aqui.

O que você escrever no formulário não sai do seu navegador: a página é estática,
não tem servidor, não envia dados para lugar nenhum e não usa cookies.

## Como usar direto do prompt

Se preferir copiar o texto na mão:

1. Abra uma conversa nova em um agente de IA **com acesso a busca na web** —
   Claude, ChatGPT ou equivalente. A busca é usada na Etapa 3, para encontrar
   vagas, programas e editais reais da região do estudante.
2. Copie o conteúdo de [`prompt.md`](prompt.md) e cole como primeira mensagem.
3. Opcionalmente, preencha os campos da seção **Informações iniciais** antes de
   enviar. Campos em branco são normais — o agente completa o que faltar durante
   a entrevista.
4. Responda às perguntas. A consultoria avança uma etapa por vez, e você pode
   mudar a ordem, pular ou aprofundar qualquer etapa a qualquer momento.

## As sete etapas

| # | Etapa | O que acontece |
|---|-------|----------------|
| 1 | Entrevista | Contexto acadêmico, interesses, bagagem real e restrições |
| 2 | Posicionamento | Objetivo profissional realista para 6 a 12 meses |
| 3 | Pesquisa de oportunidades | Busca na web por vagas, editais e caminhos na região |
| 4 | Currículo | Currículo de uma página, escrito e pronto para uso |
| 5 | LinkedIn e redes | Headline, seção "Sobre", descrições e modelos de abordagem |
| 6 | Presença própria | Site, portfólio ou repositório — só se a área exigir |
| 7 | Plano de ação | Rotina de busca e metas para 30, 60 e 90 dias |

Ao fim de cada etapa o agente entrega o resultado, resume o que ficou definido e
pergunta se pode avançar. Ele também mantém uma **Ficha do Estudante** atualizada,
reexibida a cada etapa, para você corrigir interpretações erradas.

## Regras embutidas no prompt

O prompt impõe ao agente um conjunto de restrições que existem para proteger o
estudante:

- **Nunca inventar.** Nenhuma experiência, curso, habilidade ou resultado entra
  no currículo sem confirmação do estudante.
- **Nada de genérico.** Conselho que serviria para qualquer pessoa é proibido.
  Sem informação suficiente para ser específico, o agente pergunta antes.
- **Citar fontes.** Toda oportunidade encontrada na web vem com link e data de
  referência. Sem acesso à web, o agente avisa e entrega um roteiro de busca em
  vez de inventar vagas.
- **Levar restrições a sério.** Quem trabalha, cuida de alguém, não tem carro ou
  precisa de bolsa que pague as contas recebe recomendações filtradas por isso.
- **Ser honesto sobre prazos.** Objetivo improvável no prazo pedido é dito com
  clareza, junto de um caminho intermediário. Sem promessa de resultado.
- **Não julgar.** Não ter experiência nenhuma no 5º período é comum, e é tratado
  como ponto de partida.

## Para quem é

Estudantes de graduação no Brasil, em qualquer período e qualquer curso. O prompt
calibra as recomendações pelo momento do curso — quem está no 1º período recebe
coisas diferentes de quem se forma em seis meses — e decide junto com o estudante
se a área dele realmente precisa de portfólio ou site.

## Limitações

- A qualidade da Etapa 3 depende do acesso real à web do agente usado. Sem busca,
  essa etapa vira um roteiro para o estudante executar por conta.
- Vagas e editais encontrados precisam ser verificados na fonte antes da
  candidatura. Prazos mudam.
- O prompt orienta a busca; ele não substitui os serviços de carreira da
  instituição de ensino, que costumam ter convênios e vagas que não aparecem em
  busca pública.

## O que tem neste repositório

| Arquivo | O que é |
|---|---|
| [`prompt.md`](prompt.md) | O prompt completo, em texto puro |
| [`index.html`](index.html) | A página com formulário e botão de copiar, servida pelo GitHub Pages |
| [`README.md`](README.md) | Este arquivo |

A página embute uma cópia do prompt no próprio HTML, para funcionar mesmo sem
rede. Ao editar `prompt.md`, regenere o HTML para os dois não ficarem
dessincronizados.

## Licença

[CC BY 4.0](LICENSE) — use, adapte e redistribua, inclusive comercialmente,
desde que dê o crédito.

## Contribuições

Sugestões de melhoria são bem-vindas via issue ou pull request. Adaptações para
outras realidades (ensino técnico, pós-graduação, outros países) são
especialmente interessantes.
