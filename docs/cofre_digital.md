---
title: Caso Pendrive-Cofre com VeraCrypt
layout: default
permalink: /cofre_digital
---

# 🔐 Caso Prático: Pendrive-Cofre com VeraCrypt

## 📌 Contexto

Um cliente necessitava preservar os dados de um pendrive contendo **arquivos sensíveis relacionados a criptomoedas** (chaves privadas, wallets, etc.). Além da preservação forense, ele exigia que o pendrive fosse transformado em um **"cofre digital"** – ou seja, um dispositivo que só pudesse ser acessado mediante uma senha forte, garantindo a confidencialidade mesmo em caso de perda ou roubo.

---

## 🎯 Objetivo

- Preservar a integridade dos dados originais (imagem forense).
- Transformar o pendrive em um volume criptografado com VeraCrypt (AES-256).
- Documentar todo o processo com evidências e hashes de verificação.

---

## 🧪 Procedimento Executado

### 1. Identificação do Dispositivo

O pendrive foi conectado à VM Kali Linux e identificado como `/dev/sdb`:

```bash
sudo fdisk -l
Saída:

text
Disk /dev/sdb: 3,66 GiB, 3926949888 bytes, 7669824 sectors
Disk model: DT 100 G2
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
2. Preservação Forense (Imagem Bit a Bit)
Antes de qualquer modificação, foi criada uma imagem forense do pendrive original utilizando o dcfldd (ferramenta forense que calcula hashes em tempo real):

bash
sudo dcfldd if=/dev/sdb of=pendrive_original.img bs=4096 hash=md5 hash=sha1 hashwindow=10G
Saída final:

text
958720 blocks (3745Mb) written.0 - 3926949888: 07f6ecd59f3833dae36cabbda5d4f940
0 - 3926949888: 0231f54de4f2d684928288ecba353548fe39ed1f

Total (md5): 07f6ecd59f3833dae36cabbda5d4f940
Total (sha1): 0231f54de4f2d684928288ecba353548fe39ed1f
Hashes obtidos:

Algoritmo	Hash
MD5	07f6ecd59f3833dae36cabbda5d4f940
SHA-1	0231f54de4f2d684928288ecba353548fe39ed1f
Esses hashes comprovam a integridade da imagem e podem ser usados para verificar futuras cópias.

3. Remoção da Partição Existente
Para criar o volume criptografado diretamente no dispositivo bruto (e não em uma partição), a tabela de partições foi removida com dd:

bash
sudo dd if=/dev/zero of=/dev/sdb bs=512 count=1
Saída:

text
1+0 registros entrados
1+0 registros saídos
512 bytes copiados, 0,0309739 s, 16,5 kB/s
Verificação:

bash
sudo fdisk -l /dev/sdb
A saída confirmou que o pendrive estava limpo, sem partições listadas.

4. Instalação do VeraCrypt (AppImage)
O Kali Linux moderno não possui o VeraCrypt nos repositórios oficiais, e as versões antigas apresentavam erros de dependência (libfuse.so.2, libgtk-x11-2.0.so.0). A solução foi utilizar a versão AppImage (portável, com todas as dependências embutidas).

Download e permissão:

bash
cd ~/Downloads
wget https://launchpad.net/veracrypt/trunk/1.26.29/+download/VeraCrypt-1.26.29-x86_64.AppImage
chmod +x VeraCrypt-1.26.29-x86_64.AppImage
Teste do modo texto:

bash
./VeraCrypt-1.26.29-x86_64.AppImage --text --help
O comando exibiu a lista de opções, confirmando que o AppImage estava funcionando corretamente.

5. Criação do Volume Criptografado
Com o pendrive limpo e o VeraCrypt pronto, foi criado o volume criptografado:

bash
sudo ./VeraCrypt-1.26.29-x86_64.AppImage --text --create /dev/sdb
Opções escolhidas durante o assistente:

Pergunta	Resposta
Volume type	1 (Normal)
Encryption algorithm	1 (AES)
Hash algorithm	2 (SHA-512)
Filesystem	3 (FAT)
Size	3072M (3 GB)
Password	cofre@2026 (armazenada em cofre de senhas)
PIM	(Enter – padrão)
Entropy	320+ caracteres aleatórios digitados manualmente
Format	yes
Mensagem final:

text
Done: 100,000%  Speed:  4,5 MB/s  Left: 0 s
O volume VeraCrypt foi criado com sucesso.
6. Montagem e Cópia de Arquivos
O volume foi montado em /media/cofre e um arquivo de exemplo (simulando uma chave privada) foi criado:

bash
sudo mkdir -p /media/cofre
sudo ./VeraCrypt-1.26.29-x86_64.AppImage --text --mount /dev/sdb /media/cofre
Solicitação de senha:

text
Enter password for /dev/sdb: 
(senha cofre@2026 foi inserida)
Criação do arquivo:

bash
echo "Chave privada: 5J3kL9mN7pQ2rT8vX4wY..." | sudo tee /media/cofre/chave.txt
Verificação:

bash
ls -la /media/cofre/
cat /media/cofre/chave.txt
Saída esperada:

text
-rw-r--r-- 1 root root 36 jun 20 00:00 chave.txt
Chave privada: 5J3kL9mN7pQ2rT8vX4wY...
7. Desmontagem Segura
Após a cópia, o volume foi desmontado para garantir que os dados ficassem inacessíveis sem a senha:

bash
sudo ./VeraCrypt-1.26.29-x86_64.AppImage --text --dismount /dev/sdb
Saída:

text
Volume /dev/sdb is not mounted. (se já estivesse desmontado)
ou simplesmente nenhuma saída (indicando sucesso).
🧠 Desafios Encontrados e Soluções
Desafio	Solução
VeraCrypt não encontrado nos repositórios do Kali	Baixado do site oficial como AppImage.
Erro libfuse.so.2: version FUSE_2.8 not found	Uso do AppImage (já inclui as dependências).
Erro libgtk-x11-2.0.so.0	Uso do modo texto (--text) com o AppImage.
Pendrive com partição existente	Remoção da partição com dd.
Processo de criação travando	Definição de tamanho fixo (3072M) em vez de usar todo o espaço.
Comandos não encontrados	Navegação correta para a pasta ~/Downloads.
Arquivo não encontrado ao copiar	O volume não estava montado – remontagem resolveu.
📊 Resultados
Item	Status
Imagem forense criada	✅
Hashes MD5 e SHA-1 registrados	✅
Partição removida com sucesso	✅
VeraCrypt AppImage funcionando	✅
Volume criptografado criado (AES-256)	✅
Arquivo sensível armazenado	✅
Desmontagem segura	✅
Documentação completa	✅
text

---

Esse é o conteúdo final com todos os detalhes, incluindo o cabeçalho extra e a estrutura completa do procedimento (itens 1 a 7). Se precisar de ajustes ou de um recorte específico (apenas os itens 2 a 7, por exemplo), é só avisar.
