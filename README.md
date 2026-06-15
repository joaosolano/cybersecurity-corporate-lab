# 🏢 cybersecurity-corporate-lab

<p align="center">
  <img src="logo_cybertecnica.png" alt="CyberTécnica Logo" width="200">
</p>
> Laboratório corporativo de cibersegurança simulando uma empresa real com 3 andares, segurança física e lógica integradas.

## 🎯 Sobre o Projeto

Este laboratório simula a **CyberTécnica LTDA**, uma empresa de cibersegurança com estrutura física de 3 andares:

| Andar | Função | Tecnologias | IP |
|-------|--------|-------------|-----|
| **Térreo** | Recepção / Público | Ubuntu Server + Apache + PHP | 192.168.18.29 |
| **1º Andar** | Infraestrutura / Servidores | Windows 10 + Wireshark | 192.168.18.30 |
| **Atacante** | Testes de segurança | Kali Linux | 192.168.18.31 |

## ✅ Passos já concluídos

### Infraestrutura
- [x] HD externo de 465GB formatado em exFAT
- [x] VirtualBox 7.2.8 instalado
- [x] Estrutura de pastas organizada

### Térreo (Recepção)
- [x] Ubuntu Server instalado
- [x] Apache + PHP configurados
- [x] Formulário de pré-cadastro de visitantes funcionando
- [x] Design profissional com CSS

### 1º Andar (Infraestrutura)
- [x] Windows 10 instalado
- [x] Rede Bridge configurada
- [x] Wireshark instalado e configurado
- [x] Firewall liberado para ping (ICMP)

### Atacante (Kali Linux)
- [x] Kali Linux instalado
- [x] Rede Bridge configurada
- [x] Nmap instalado
- [x] Testes de comunicação com Térreo e 1º Andar
- [x] Escaneamento de portas
- [x] Detecção de sistema operacional (Windows 10 - 97% de precisão)
- [x] Testes de vulnerabilidade SMB

## 📸 Evidências da Implementação

### Configuração do Laboratório

| Etapa | Screenshot |
|-------|------------|
| Estrutura de pastas do HD | ![Pastas](screenshots/01-pastas.png.png) |
| VirtualBox com Kali | ![VirtualBox](screenshots/02-virtualbox.png.png) |
| Kali Linux rodando | ![Kali Desktop](screenshots/03-kali-desktop.png.png) |
| Comando whoami | ![whoami](screenshots/04-kali-whoami.png.png) |
| Comando ip a | ![ip a](screenshots/05-kali-ip.png.png) |

### Térreo - Servidor Ubuntu (Recepção)

| Etapa | Screenshot |
|-------|------------|
| Login no Ubuntu Server | ![Login](screenshots/06-ubuntu-login.png) |
| Apache instalado | ![Apache](screenshots/07-apache-instalado.png) |
| Página padrão do Apache | ![Apache Padrão](screenshots/08-pagina-padrao-apache.png.png) |
| Formulário da Recepção | ![Formulário Vazio](screenshots/09-formulario-bonito-vazio.png.png) |
| Formulário preenchido | ![Formulário Preenchido](screenshots/10-formulario-preenchido.png.png) |

### 1º Andar - Windows 10 (Infraestrutura)

| Etapa | Screenshot |
|-------|------------|
| Wireshark instalado | ![Wireshark](screenshots/11-wireshark-instalado.png.png) |
| Wireshark capturando ping | ![Captura](screenshots/12-wireshark-capturando-ping.png.png) |
| Ping para o Térreo (Ubuntu) | ![Ping](screenshots/13-windows-ping-ubuntu.png.png) |
| Filtro ICMP aplicado | ![Filtro ICMP](screenshots/14-wireshark-filtro-icmp.png.png) |

### Atacante - Kali Linux (Testes de Segurança)

| Etapa | Screenshot |
|-------|------------|
| Ping para o Ubuntu (Térreo) | ![Ping Ubuntu](screenshots/15-kali-ping-ubuntu.png.png) |
| Ping para o Windows (1º Andar) | ![Ping Windows](screenshots/16-kali-ping-windows.png.png) |
| Escaneamento de rede | ![Scan Network](screenshots/17-nmap-scan-network.png.png) |
| Escaneamento do Ubuntu (porta 80) | ![Scan Ubuntu](screenshots/18-nmap-scan-ubuntu.png.png) |
| Escaneamento do Windows (SMB) | ![Scan Windows](screenshots/19-nmap-scan-windows.png.png) |
| Teste de vulnerabilidade SMB | ![SMB Vuln](screenshots/20-nmap-smb-vuln.png.png) |
| Detecção de SO (Windows 10 97%) | ![OS Detection](screenshots/21-nmap-os-detection.png.png) |

## 🛠️ Técnicas e Ferramentas Utilizadas

| Categoria | Ferramentas | Técnicas |
|-----------|-------------|----------|
| **Virtualização** | VirtualBox | VMs portáteis em HD externo |
| **Sistemas** | Kali Linux, Ubuntu, Windows 10 | 3 andares interconectados |
| **Rede** | Bridge mode, NAT | Comunicação entre VMs |
| **Serviços** | Apache2, PHP | Site da recepção |
| **Análise** | Wireshark | Captura de pacotes ICMP, SYN/SYN-ACK |
| **Pentest** | Nmap | Escaneamento, detecção de SO, vulnerabilidades |

## 🚀 Próximos passos

- [ ] Configurar firewall pfSense (separar andares logicamente)
- [ ] Modelagem 3D do prédio no FreeCAD
- [ ] Simular ataques avançados (Metasploit)
- [ ] Configurar IDS/IPS (Snort/Suricata)

## 👤 Autor

**João Solano**

Projeto em desenvolvimento como parte do portfólio prático em cibersegurança.

🔗 [GitHub](https://github.com/joaosolano/cybersecurity-corporate-lab)
