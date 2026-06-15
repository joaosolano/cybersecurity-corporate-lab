# 🔐 CyberTécnica LTDA – Laboratório de Cibersegurança  
**Documentação completa do projeto – passo a passo e aprendizados**

> **Status:** Em andamento  
> **Objetivo:** Simular uma empresa real com 3 andares (térreo, infraestrutura, diretoria), integrando segurança física (modelagem 3D) e lógica (redes, firewalls, ataques controlados).

---

## 📌 Resumo do Projeto

Este laboratório foi construído do zero em um **HD externo de 465GB** formatado em **exFAT** para portabilidade. Utilizando **VirtualBox**, foram criadas 3 máquinas virtuais:

| Andar | Sistema | IP | Função |
|-------|---------|----|--------|
| Térreo | Ubuntu Server 22.04 | 192.168.18.29 | Recepção (formulário PHP) |
| 1º Andar | Windows 10 Pro | 192.168.18.30 | Infraestrutura (Wireshark) |
| Atacante | Kali Linux | 192.168.18.31 | Testes de segurança (Nmap) |

- O **Térreo** roda um servidor Apache/PHP com formulário de pré-cadastro de visitantes (design profissional).
- O **1º Andar** possui o **Wireshark** para captura de tráfego.
- O **Kali Linux** foi usado para escanear a rede, descobrir portas abertas e identificar o sistema operacional (97% de acerto).

A comunicação entre as VMs foi garantida pelo modo **Bridge** no VirtualBox, após ajustes no firewall do Windows para liberar o ICMP (ping).

A documentação completa está neste repositório, com todas as capturas de tela organizadas na pasta `screenshots`.

---

## 🧠 Aprendizados e Desafios Técnicos

| Desafio | Solução |
|---------|---------|
| Nome de usuário incorreto no login do Kali | Reinstalação cuidadosa, anotação das credenciais |
| Layout de teclado do Ubuntu Server (US vs BR) | Configuração manual com `sudo localectl set-keymap br` |
| VirtualBox sem área de transferência compartilhada | Instalação dos Guest Additions e uso de rede Bridge para SSH |
| Lentidão da internet no Windows 10 (VM) | Troca da versão do VirtualBox (7.2.8 → 7.1.18) |
| Firewall do Windows bloqueando ping (ICMP) | Comando `netsh advfirewall firewall add rule name="Liberar Ping" protocol=icmpv4 dir=in action=allow` |

---

## 🧩 Passo a Passo Detalhado

### 1. Preparação do HD externo
- Formatação em **exFAT** (rótulo `LAB_CYBER`) para suportar arquivos grandes (>4GB).
- Criação da estrutura de pastas: `01_VirtualBox`, `02_VMs`, `03_ISOs`, `04_Projeto_3D`, `05_Documentos_Empresa`, `06_Ferramentas`.

### 2. Instalação do VirtualBox e VMs
- VirtualBox 7.2.8 (após ajuste, versão 7.1.18 para estabilidade de rede).
- Criadas as VMs com as seguintes especificações:
  - **Kali Linux:** 2GB RAM, 30GB disco, rede Bridge.
  - **Ubuntu Server:** 1GB RAM, 20GB disco, rede Bridge.
  - **Windows 10:** 4GB RAM, 64GB disco, rede Bridge.

### 3. Configuração do Térreo (Ubuntu Server)
- Instalação do Apache e PHP:
  ```bash
  sudo apt update && sudo apt install apache2 php libapache2-mod-php -y
