# 🏢 cybersecurity-corporate-lab

> Laboratório corporativo de cibersegurança simulando uma empresa real com 3 andares, segurança física e lógica integradas.

## 🎯 Sobre o Projeto

Este laboratório simula a **CyberTécnica LTDA**, uma empresa de cibersegurança com estrutura física de 3 andares:

| Andar | Função | Tecnologias |
|-------|--------|-------------|
| **Térreo** | Recepção / Público | Ubuntu Server + Apache + PHP |
| **1º Andar** | Infraestrutura / Servidores | Windows 10 + Wireshark |
| **2º Andar** | Diretoria | Windows 10 (em breve) |

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
- [x] Rede Bridge configurada (IP: 192.168.18.30)
- [x] Wireshark instalado
- [x] Teste de ping para o Térreo (Ubuntu: 192.168.18.29)
- [x] Captura de pacotes ICMP no Wireshark

### Atacante
- [x] Kali Linux instalado
- [x] Snapshot do sistema limpo salvo

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

## 🚀 Próximos passos

- [ ] Verificar IP do Kali Linux e conectar à mesma rede
- [ ] Simular primeiro ataque controlado (Kali → Ubuntu)
- [ ] Analisar ataque no Wireshark
- [ ] Configurar firewall pfSense
- [ ] Modelagem 3D do prédio no FreeCAD

## 👤 Autor

**João Solano**

Projeto em desenvolvimento como parte do portfólio prático em cibersegurança.

🔗 [GitHub](https://github.com/joaosolano/cybersecurity-corporate-lab)
