---
title: "Caso Pendrive-Cofre com VeraCrypt"
layout: default
permalink: /cofre_digital/
---

# 🔐 Caso Prático: Pendrive-Cofre com VeraCrypt

## 📌 Contexto

Um cliente necessitava preservar os dados de um pendrive contendo **arquivos sensíveis relacionados a criptomoedas**...

Além da preservação forense, foi solicitado que o dispositivo fosse transformado em um verdadeiro **cofre digital**, permitindo acesso somente mediante autenticação por senha forte, garantindo a confidencialidade dos dados mesmo em caso de perda, furto ou acesso não autorizado.

O projeto exigiu a combinação de técnicas de **computação forense**, **preservação de evidências digitais** e **criptografia avançada**, utilizando ferramentas amplamente reconhecidas na área de segurança da informação.

---

# 🎯 Objetivos

O procedimento foi planejado para atingir os seguintes objetivos:

* Preservar integralmente os dados originais do dispositivo.
* Produzir uma imagem forense bit a bit do pendrive.
* Gerar hashes criptográficos para validação futura.
* Eliminar riscos de alteração dos dados durante o processo.
* Transformar o dispositivo em um volume criptografado utilizando VeraCrypt.
* Utilizar algoritmos modernos de criptografia.
* Documentar todas as etapas para fins de auditoria e rastreabilidade.
* Garantir confidencialidade, integridade e autenticidade das informações armazenadas.

---

# 🧪 Procedimento Executado

## 1. Identificação do Dispositivo

Após conectar o pendrive à máquina virtual Kali Linux, foi realizada sua identificação utilizando a ferramenta `fdisk`.

### Comando

```bash
sudo fdisk -l
```

### Saída Obtida

```text
Disk /dev/sdb: 3.66 GiB, 3926949888 bytes, 7669824 sectors
Disk model: DT 100 G2

Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

Foi confirmado que o dispositivo correspondente ao pendrive era:

```text
/dev/sdb
```

---

## 2. Preservação Forense (Imagem Bit a Bit)

Antes de qualquer alteração estrutural no dispositivo, foi realizada sua aquisição forense utilizando a ferramenta **dcfldd**, uma evolução do utilitário tradicional `dd`, amplamente utilizada em laboratórios de perícia digital.

Além da cópia bit a bit, a ferramenta permite gerar hashes durante a aquisição, possibilitando a verificação posterior da integridade da imagem.

### Comando Utilizado

```bash
sudo dcfldd if=/dev/sdb of=pendrive_original.img bs=4096 hash=md5 hash=sha1 hashwindow=10G
```

### Saída Final

```text
958720 blocks (3745Mb) written.

0 - 3926949888: 07f6ecd59f3833dae36cabbda5d4f940
0 - 3926949888: 0231f54de4f2d684928288ecba353548fe39ed1f

Total (md5): 07f6ecd59f3833dae36cabbda5d4f940
Total (sha1): 0231f54de4f2d684928288ecba353548fe39ed1f
```

### Hashes Obtidos

| Algoritmo | Hash                                       |
| --------- | ------------------------------------------ |
| MD5       | `07f6ecd59f3833dae36cabbda5d4f940`         |
| SHA-1     | `0231f54de4f2d684928288ecba353548fe39ed1f` |

Esses hashes permitem comprovar que a imagem forense permanece íntegra ao longo do tempo.

Qualquer alteração, mesmo de um único byte, resultará em um hash completamente diferente.

### Evidência de Preservação

A geração da imagem forense antes de qualquer modificação garante:

* Preservação da evidência original.
* Possibilidade de recuperação futura dos dados.
* Reprodutibilidade do procedimento.
* Cadeia de custódia digital.
* Conformidade com boas práticas de perícia computacional.

---

## 3. Remoção da Tabela de Partições

Após a conclusão da aquisição forense, o dispositivo foi preparado para receber um volume criptografado VeraCrypt.

Optou-se por utilizar o dispositivo bruto (*raw device*), sem partições intermediárias, reduzindo a superfície de exposição de metadados e simplificando a administração do volume.

Para isso, a tabela de partições existente foi removida sobrescrevendo os primeiros 512 bytes do dispositivo.

### Comando Utilizado

```bash
sudo dd if=/dev/zero of=/dev/sdb bs=512 count=1
```

### Saída Obtida

```text
1+0 registros entrados
1+0 registros saídos
512 bytes copiados, 0,0309739 s, 16,5 kB/s
```

### Verificação

```bash
sudo fdisk -l /dev/sdb
```

A saída confirmou a inexistência de partições reconhecidas no dispositivo.

### Aprendizado

A remoção da tabela de partições não apaga integralmente os dados do pendrive, mas elimina as estruturas responsáveis pelo seu reconhecimento pelo sistema operacional.

Como já havia sido produzida uma imagem forense completa, a integridade dos dados originais permaneceu preservada.

---

## 4. Instalação do VeraCrypt

O objetivo seguinte consistiu em transformar o dispositivo em um cofre digital protegido por criptografia forte.

Durante os testes verificou-se que as versões disponíveis em alguns repositórios apresentavam problemas de compatibilidade e dependências ausentes, incluindo:

* `libfuse.so.2`
* `libgtk-x11-2.0.so.0`

Para evitar conflitos de bibliotecas e simplificar a instalação, optou-se pela utilização da versão AppImage do VeraCrypt.

### Download

```bash
cd ~/Downloads

wget https://launchpad.net/veracrypt/trunk/1.26.29/+download/VeraCrypt-1.26.29-x86_64.AppImage
```

### Permissão de Execução

```bash
chmod +x VeraCrypt-1.26.29-x86_64.AppImage
```

### Teste de Funcionamento

```bash
./VeraCrypt-1.26.29-x86_64.AppImage --text --help
```

O comando exibiu corretamente a lista de opções disponíveis, comprovando que o aplicativo estava operacional.

### Vantagens da Utilização do AppImage

* Não requer instalação convencional.
* Dispensa dependências externas complexas.
* Facilita a portabilidade entre sistemas Linux.
* Mantém maior compatibilidade entre distribuições.
* Reduz o risco de conflitos de bibliotecas.

---

## 5. Criação do Volume Criptografado

Com o dispositivo preparado, foi iniciado o assistente de criação do volume VeraCrypt.

### Comando Utilizado

```bash
sudo ./VeraCrypt-1.26.29-x86_64.AppImage --text --create /dev/sdb
```

Durante o processo foram definidas as seguintes configurações.

### Configurações Selecionadas

| Parâmetro                 | Valor                                    |
| ------------------------- | ---------------------------------------- |
| Tipo de Volume            | Normal                                   |
| Algoritmo de Criptografia | AES                                      |
| Algoritmo de Hash         | SHA-512                                  |
| Sistema de Arquivos       | FAT                                      |
| Tamanho do Volume         | 3072 MB                                  |
| Senha                     | Definida pelo cliente                    |
| PIM                       | Padrão                                   |
| Entropia                  | Entrada manual superior a 320 caracteres |

### Geração de Entropia

Uma das etapas mais importantes consistiu na geração de entropia para a criação das chaves criptográficas.

Foram digitados manualmente mais de 320 caracteres aleatórios, aumentando significativamente a qualidade dos números pseudoaleatórios utilizados na geração das chaves.

Essa etapa reduz riscos relacionados à previsibilidade criptográfica.

### Formatação do Volume

Após a confirmação das configurações, o VeraCrypt realizou a criação do sistema de arquivos criptografado.

### Saída Final

```text
Done: 100.000%
Speed: 4.5 MB/s
Left: 0 s
```

### Resultado

Ao término do processo, o pendrive passou a operar como um volume VeraCrypt protegido por criptografia AES, exigindo autenticação para qualquer acesso ao conteúdo armazenado.

Sem a senha correta, os dados permanecem inacessíveis e indistinguíveis de dados aleatórios.

---

## Considerações Técnicas sobre a Criptografia Utilizada

O algoritmo AES (Advanced Encryption Standard) é atualmente um dos padrões criptográficos mais utilizados no mundo, sendo empregado por organizações governamentais, instituições financeiras e empresas de tecnologia.

Características relevantes:

* Chave criptográfica de alta robustez.
* Excelente desempenho em hardware moderno.
* Ampla auditoria pela comunidade acadêmica.
* Resistência conhecida contra ataques práticos atuais.

O algoritmo SHA-512 foi utilizado como função de derivação e verificação, fornecendo maior robustez na geração de chaves.

A combinação AES + SHA-512 oferece elevado nível de segurança para armazenamento de informações sensíveis.

---


## 6. Montagem do Volume Criptografado

Após a criação do volume VeraCrypt, foi realizado um teste completo de acesso para validar o funcionamento do cofre digital.

Inicialmente foi criado um ponto de montagem no sistema operacional.

### Criação do Diretório

```bash id="6r8mzp"
sudo mkdir -p /media/cofre
```

### Montagem do Volume

```bash id="2yhq9j"
sudo ./VeraCrypt-1.26.29-x86_64.AppImage --text --mount /dev/sdb /media/cofre
```

### Solicitação de Senha

```text id="1xv5gt"
Enter password for /dev/sdb:
```

Após a autenticação bem-sucedida, o volume foi disponibilizado normalmente no diretório especificado.

---

## 7. Teste de Escrita e Leitura

Para validar o funcionamento do volume criptografado, foi criado um arquivo de teste simulando um documento sensível.

### Criação do Arquivo

```bash id="9b2qtr"
echo "Chave privada: EXEMPLO_DE_DADOS_SENSIVEIS" | sudo tee /media/cofre/chave.txt
```

### Verificação do Conteúdo

```bash id="7j2mny"
cat /media/cofre/chave.txt
```

### Resultado

```text id="2b2xqn"
Chave privada: EXEMPLO_DE_DADOS_SENSIVEIS
```

### Listagem dos Arquivos

```bash id="c5evyn"
ls -lah /media/cofre
```

A leitura e escrita ocorreram normalmente, comprovando o correto funcionamento do sistema de arquivos criptografado.

---

## 8. Desmontagem Segura

Após a validação do acesso, o volume foi desmontado para impedir qualquer leitura sem autenticação.

### Comando

```bash id="m5fwv3"
sudo ./VeraCrypt-1.26.29-x86_64.AppImage --text --dismount /dev/sdb
```

Dependendo da versão utilizada, o VeraCrypt pode exibir:

```text id="1f8n8v"
Volume /dev/sdb is not mounted.
```

ou simplesmente retornar ao prompt sem mensagens adicionais.

### Objetivo da Desmontagem

A desmontagem segura garante que:

* As chaves criptográficas sejam removidas da memória.
* O sistema de arquivos seja encerrado corretamente.
* Não ocorram corrupções de dados.
* O conteúdo permaneça inacessível sem autenticação.

---

# ⚠️ Desafios Encontrados e Soluções Aplicadas

Durante a execução do projeto foram encontrados alguns obstáculos técnicos.

| Desafio                                             | Solução Aplicada                                     |
| --------------------------------------------------- | ---------------------------------------------------- |
| Dependências ausentes do VeraCrypt nos repositórios | Utilização da versão AppImage                        |
| Erros relacionados ao FUSE                          | Uso da versão portátil com dependências incorporadas |
| Reconhecimento incorreto do dispositivo             | Verificação manual via fdisk                         |
| Necessidade de preservar os dados originais         | Aquisição forense prévia com dcfldd                  |
| Garantia de integridade dos dados                   | Geração de hashes MD5 e SHA-1                        |
| Segurança do armazenamento                          | Implementação de criptografia VeraCrypt AES          |

---

# 📊 Resultados Obtidos

| Objetivo                                     | Status      |
| -------------------------------------------- | ----------- |
| Identificação correta do dispositivo         | ✅ Concluído |
| Aquisição forense bit a bit                  | ✅ Concluído |
| Geração de hashes de integridade             | ✅ Concluído |
| Preservação dos dados originais              | ✅ Concluído |
| Remoção da estrutura anterior do dispositivo | ✅ Concluído |
| Instalação do VeraCrypt                      | ✅ Concluído |
| Criação do volume criptografado              | ✅ Concluído |
| Teste de escrita e leitura                   | ✅ Concluído |
| Desmontagem segura                           | ✅ Concluído |
| Documentação do procedimento                 | ✅ Concluído |

---

# 🔍 Validação da Integridade

Os hashes gerados durante a aquisição forense permanecem como referência para futuras validações.

| Algoritmo | Hash                                       |
| --------- | ------------------------------------------ |
| MD5       | `07f6ecd59f3833dae36cabbda5d4f940`         |
| SHA-1     | `0231f54de4f2d684928288ecba353548fe39ed1f` |

Esses valores permitem confirmar a autenticidade da imagem original e detectar qualquer modificação posterior.

---

# 📚 Lições Aprendidas

Este projeto demonstrou a importância da integração entre técnicas de computação forense e segurança da informação.

Principais aprendizados:

* Nunca alterar a mídia original antes da aquisição forense.
* Registrar todas as etapas executadas.
* Utilizar múltiplos hashes para validação.
* Testar o processo completo antes da entrega ao cliente.
* Priorizar soluções criptográficas amplamente auditadas.
* Documentar decisões técnicas e justificativas.

---

# 🔐 Considerações sobre Segurança

A política adotada neste projeto pode ser resumida como:

> **Preservar primeiro, modificar depois.**

A imagem forense garante a recuperação futura dos dados originais, enquanto o volume VeraCrypt protege o conteúdo operacional utilizado pelo cliente.

O conceito é semelhante ao utilizado em ambientes corporativos de alta segurança:

* Evidência preservada.
* Dados protegidos.
* Acesso controlado.
* Integridade verificável.

---

# 🏁 Conclusão

O objetivo do projeto foi alcançado com sucesso.

A mídia original foi preservada por meio de uma aquisição forense completa, acompanhada de hashes criptográficos para validação futura.

Posteriormente, o dispositivo foi convertido em um cofre digital utilizando VeraCrypt com criptografia AES e autenticação por senha, proporcionando um ambiente seguro para armazenamento de informações sensíveis relacionadas a criptomoedas.

A combinação entre preservação forense e criptografia forte permitiu atender simultaneamente aos requisitos de integridade, confidencialidade e rastreabilidade exigidos pelo cliente.

Este caso demonstra como ferramentas amplamente utilizadas na área de perícia computacional e segurança da informação podem ser integradas para produzir soluções práticas, auditáveis e tecnicamente robustas.

---

## 👨‍💻 Ferramentas Utilizadas

* Kali Linux
* dcfldd
* fdisk
* dd
* VeraCrypt AppImage
* SHA-1
* MD5
* AES
* Sistema de Arquivos FAT

---

**Autor:** João Solano
**Área:** Computação Forense • Segurança da Informação • Criptografia
**Data do Projeto:** 2026
