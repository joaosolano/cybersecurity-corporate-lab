---
layout: default
title: pfSense / Firewall Corporativo
permalink: /docs/pfsense/
---

# 🔥 pfSense / Firewall Corporativo – CyberTécnica LTDA

## O que é o pfSense?

O **pfSense** é um firewall/open-source de classe empresarial, baseado no FreeBSD. Ele é amplamente utilizado para roteamento, segurança de rede e criação de VPNs, sendo uma solução gratuita e extremamente poderosa para ambientes corporativos e laboratórios de segurança.

---

## Por que o pfSense no CyberTécnica?

No laboratório da CyberTécnica, o pfSense foi escolhido para implementar a **separação lógica dos 3 andares da empresa**, criando zonas de rede isoladas com regras de firewall específicas para cada setor.

Com ele, é possível simular um ambiente corporativo real, onde:

- O **Térreo (Recepção)** e o **1º Andar (Infraestrutura)** ficam em uma rede interna (LAN).
- O **2º Andar (Diretoria / SCIF)** fica em uma rede isolada (OPT1).
- **Servidores públicos** podem ser alocados em uma zona DMZ (OPT2), futuramente.

---

## 🏗️ Estrutura de Redes Planejada

| Interface | Rede            | Finalidade                         |
|-----------|-----------------|------------------------------------|
| **WAN**   | NAT (Host)      | Acesso à internet simulada         |
| **LAN**   | `192.168.1.0/24`| Térreo (Recepção) + 1º Andar (TI)  |
| **OPT1**  | `192.168.3.0/24`| 2º Andar (Diretoria / SCIF)        |
| **OPT2**  | `192.168.2.0/24`| DMZ (servidores públicos – futuro) |

---

## ✅ Etapas Implementadas

### 1. Criação das Redes Internas no VirtualBox

Foram criadas as seguintes redes internas (Internal Network) no VirtualBox:

| Nome da Rede       | Finalidade                     |
|--------------------|--------------------------------|
| `intnet_lan`       | Térreo + 1º Andar              |
| `intnet_diretoria` | 2º Andar (Diretoria)           |
| `intnet_dmz`       | DMZ (servidores futuros)       |

### 2. Criação da VM do pfSense

Uma máquina virtual dedicada foi criada com as seguintes configurações:

| Configuração      | Valor                          |
|-------------------|--------------------------------|
| **Nome**          | `pfSense_Firewall`             |
| **Pasta**         | `E:\02_VMs\pfSense_Firewall`   |
| **Tipo**          | BSD                            |
| **Versão**        | FreeBSD (64-bit)               |
| **RAM**           | 2048 MB (2GB)                  |
| **Disco**         | VDI, 20 GB, dinamicamente alocado |
| **Adaptadores**   | 4 (WAN, LAN, OPT1, OPT2)       |

### 3. Instalação e Configuração Inicial

O pfSense foi instalado a partir da ISO oficial (`pfSense-CE-2.7.2-RELEASE-amd64.iso`). Durante a configuração inicial:

- As interfaces foram atribuídas no console:
  - **WAN** → Adaptador 1 (NAT)
  - **LAN** → Adaptador 2 (`intnet_lan`)
  - **OPT1** → Adaptador 3 (`intnet_diretoria`)
  - **OPT2** → Adaptador 4 (`intnet_dmz`)
- A interface LAN foi configurada com o IP `192.168.1.1/24`.
- A interface OPT1 foi configurada com o IP `192.168.3.1/24`.
- A interface OPT2 foi configurada com o IP `192.168.2.1/24`.

### 4. Acesso à Interface Web

A administração do firewall é feita via navegador, acessando:



Login padrão:
- **Usuário:** `admin`
- **Senha:** `pfsense` (alterada após o primeiro acesso)

### 5. Configuração de DHCP

Foram habilitados servidores DHCP para cada rede interna:

| Interface | Range de IPs               |
|-----------|----------------------------|
| **LAN**   | `192.168.1.100 – 192.168.1.200` |
| **OPT1**  | `192.168.3.100 – 192.168.3.200` |

### 6. Regras de Firewall

Foram aplicadas regras de firewall para garantir o isolamento entre os andares:

| Origem       | Destino               | Ação    | Descrição                      |
|--------------|-----------------------|---------|--------------------------------|
| **LAN**      | Qualquer              | Allow   | Térreo e TI acessam tudo       |
| **OPT1**     | Qualquer              | Allow   | Diretoria acessa tudo          |
| **LAN**      | `192.168.3.0/24`      | Block   | Bloqueia acesso LAN → Diretoria |
| **WAN**      | Qualquer              | Deny    | Bloqueia acesso externo direto |

### 7. Integração com as VMs

As VMs existentes foram reconectadas às redes internas:

| VM            | Rede Conectada     | IP Atribuído (via DHCP) |
|---------------|--------------------|--------------------------|
| **Ubuntu**    | `intnet_lan`       | `192.168.1.xxx`          |
| **Windows 10**| `intnet_lan`       | `192.168.1.xxx`          |
| **Kali Linux**| Bridge (externa)   | `192.168.18.xxx` (manualmente) |

> **Nota:** O Kali permanece em Bridge para simular um atacante externo à rede corporativa.

---

## 🧪 Testes Realizados

- **Ping da LAN para o pfSense:** `ping 192.168.1.1` → ✅ Sucesso
- **Ping da LAN para a internet (via WAN):** `ping 8.8.8.8` → ✅ Sucesso (com regra NAT)
- **Ping da LAN para a Diretoria (OPT1):** `ping 192.168.3.1` → ❌ Bloqueado (regra de firewall)
- **Ping da Diretoria para a LAN:** `ping 192.168.1.1` → ✅ Sucesso (regra Allow)

---

## 📸 Evidências

As seguintes capturas de tela foram documentadas:

| Etapa | Arquivo |
|-------|---------|
| Criação das redes internas no VirtualBox | `screenshots/pfsense/pfsense-redes-internas.png` |
| Instalação do pfSense | `screenshots/pfsense/pfsense-instalacao.png` |
| Atribuição de interfaces no console | `screenshots/pfsense/pfsense-interfaces.png` |
| Interface web do pfSense (dashboard) | `screenshots/pfsense/pfsense-dashboard.png` |
| Configuração de DHCP | `screenshots/pfsense/pfsense-dhcp.png` |
| Regras de firewall | `screenshots/pfsense/pfsense-firewall-rules.png` |
| Teste de ping da LAN para o pfSense | `screenshots/pfsense/pfsense-ping-lan.png` |
| Teste de ping bloqueado para a Diretoria | `screenshots/pfsense/pfsense-ping-blocked.png` |

---

## ✅ Benefícios Alcançados

- **Isolamento Lógico**: A Diretoria (2º andar) agora está em uma rede separada, com acesso restrito e controlado.
- **Controle Granular**: É possível definir exatamente quais serviços e portas são permitidos entre os andares.
- **Simulação Realista**: O laboratório reproduz com fidelidade a arquitetura de segurança de uma empresa de médio porte.
- **Aprendizado Prático**: A configuração e o gerenciamento do pfSense proporcionam uma experiência valiosa em administração de redes e firewalls.

---

## 🚀 Próximos Passos (Planejados)

- [ ] Configurar **VPN** (OpenVPN) para acesso remoto seguro à rede corporativa
- [ ] Implementar **regras avançadas** de firewall (ex.: restringir acesso da DMZ à LAN)
- [ ] Instalar **Snort/Suricata** como IDS/IPS no pfSense
- [ ] Configurar **balanceamento de carga** e **alta disponibilidade** (em estudos)
- [ ] Documentar procedimentos de **backup e restauração** das configurações do pfSense

---

## 📚 Links Úteis

- [Documentação Oficial do pfSense](https://docs.netgate.com/pfsense/en/latest/)
- [Comunidade pfSense](https://www.reddit.com/r/PFSENSE/)
- [Guia de Configuração de Firewall](https://docs.netgate.com/pfsense/en/latest/firewall/index.html)

---

**Última atualização:** Junho de 2026
