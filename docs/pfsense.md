---
title: pfSense – Firewall Corporativo
layout: default
permalink: /pfsense
---

# 🔥 pfSense – Firewall do CyberTécnica

## 📌 Objetivo

Implementar o **pfSense** como firewall principal do laboratório, responsável por:

- Segmentar a rede em VLANs para isolar os três andares
- Controlar o tráfego entre setores (Recepção, TI, Diretoria)
- Implementar regras de segurança (DMZ, NAT, bloqueios)
- Servir como gateway e firewall para as VMs do laboratório

---

## 🧱 Arquitetura de Rede

| Interface | Função | Rede / VLAN | Conectividade |
|-----------|--------|-------------|---------------|
| **WAN** | Conexão com a internet | Bridge (rede física do host) | Acesso à internet |
| **LAN** | Rede interna (Kali + andares) | `192.168.1.0/24` | Kali Linux, VMs |
| **OPT1** | Térreo (Recepção) | `192.168.10.0/24` | Ubuntu Server |
| **OPT2** | 1º Andar (TI) | `192.168.20.0/24` | Windows 10 |
| **OPT3** | 2º Andar (Diretoria) | `192.168.30.0/24` | Windows 10 (futuro) |

---

## 🔧 Configurações Realizadas

### ✅ Concluído

- [x] Download da ISO do pfSense (versão Community Edition)
- [x] Criação da VM no VirtualBox com 3 adaptadores de rede
- [x] Instalação do pfSense na VM
- [x] Atribuição das interfaces (WAN, LAN, OPT1)
- [x] Acesso ao Web Configurator (`https://192.168.1.1`)
- [x] Login inicial (usuário `admin` / senha `pfsense`)
- [x] Configuração inicial (hostname, DNS, timezone)
- [x] Configuração das VLANs para cada andar
- [x] Criação de regras de firewall (bloqueios entre andares)
- [x] Testes de conectividade entre as VMs
- [x] Isolamento lógico dos três andares

---

## 📋 Regras de Firewall Implementadas

A política de firewall segue o princípio do **menor privilégio**:

| Origem | Destino | Ação | Justificativa |
|--------|---------|------|---------------|
| **LAN (Kali)** | WAN | ✅ Liberado | Acesso à internet |
| **LAN (Kali)** | OPT1, OPT2, OPT3 | ✅ Bloqueado | Kali não acessa os andares |
| **OPT1 (Térreo)** | WAN | ✅ Liberado | Recepção precisa da internet |
| **OPT1 (Térreo)** | LAN, OPT2, OPT3 | ✅ Bloqueado | Isolamento do Térreo |
| **OPT2 (TI)** | WAN | ✅ Liberado | TI precisa da internet |
| **OPT2 (TI)** | OPT1 | ✅ Liberado (HTTP/HTTPS) | TI mantém site da recepção |
| **OPT3 (Diretoria)** | WAN | ✅ Liberado | Diretoria precisa da internet |
| **OPT3 (Diretoria)** | OPT1, OPT2, LAN | ✅ Bloqueado | Isolamento da Diretoria |

---

## 🖥️ Comandos e Ferramentas Utilizados

- **Instalação da VM**: VirtualBox 7.2.8
- **ISO utilizada**: `pfSense-CE-2.7.2-RELEASE-amd64.iso`
- **Acesso ao Web Configurator**: via Kali Linux (`https://192.168.1.1`)
- **Testes de conectividade**: `ping` entre as VMs

---

## 🧠 Lições Aprendidas

- O pfSense exige pelo menos **2 interfaces de rede** para funcionar como firewall (WAN + LAN).
- A atribuição correta das interfaces no primeiro boot é fundamental.
- O Web Configurator só é acessível pela interface LAN.
- VLANs no pfSense exigem configuração adicional no VirtualBox (adaptadores com tags).
- O princípio do menor privilégio é essencial para uma política de firewall eficaz.

---

## 📸 Evidências

- [ ] Capturas de tela da instalação
- [ ] Capturas das regras de firewall
- [ ] Testes de conectividade entre as VMs

---

## 🔗 Links Relacionados

- [Documentação Oficial do pfSense](https://docs.netgate.com/pfsense/en/latest/)
- [pfSense no VirtualBox – Guia](https://www.netgate.com/docs/pfsense/en/latest/installation/installing-pfsense-on-virtualbox.html)
- [Página Inicial do CyberTécnica](/)
- [Evidências do Laboratório](evidencias)

---

**Responsável:** João Solano  
**Data de conclusão:** Junho de 2026  
**Status:** ✅ Concluído

---

📎 [Voltar à página inicial](/)
