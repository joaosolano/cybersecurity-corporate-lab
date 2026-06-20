# 🏢 CyberTécnica LTDA – Laboratório Corporativo de Cibersegurança

<p align="center">
  <img src="logo_cybertecnica.png" alt="CyberTécnica Logo" width="220">
</p>

<p align="center">
  <strong>
    Um laboratório corporativo de cibersegurança desenvolvido para simular uma empresa real,
    integrando infraestrutura, redes, segurança física, segurança lógica,
    computação forense e testes ofensivos em um ambiente totalmente portátil.
  </strong>
</p>

<p align="center">

<a href="https://github.com/joaosolano/cybersecurity-corporate-lab">
<img src="https://img.shields.io/badge/Repositório-GitHub-blue?style=flat-square&logo=github">
</a>

<a href="https://joaosolano.github.io/cybersecurity-corporate-lab/">
<img src="https://img.shields.io/badge/Site-GitHub%20Pages-brightgreen?style=flat-square&logo=githubpages">
</a>

<a href="https://github.com/joaosolano/cybersecurity-corporate-lab/blob/main/LICENSE">
<img src="https://img.shields.io/badge/Licença-MIT-green?style=flat-square">
</a>

<a href="https://www.linkedin.com/in/joão-solano-310774138/">
<img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin">
</a>

</p>

---

# 🎯 Sobre o Projeto

O **CyberTécnica LTDA** é um laboratório de cibersegurança construído para reproduzir o funcionamento de uma empresa real.

Ao invés de utilizar apenas máquinas virtuais isoladas, o projeto simula uma infraestrutura corporativa completa, composta por diferentes setores, serviços, políticas de segurança e cenários de ataque e defesa.

Todo o ambiente foi desenvolvido para ser **portátil**, funcionando integralmente em um **HD externo**, permitindo demonstrações, estudos e experimentações em qualquer computador compatível.

O objetivo principal é consolidar conhecimentos práticos nas áreas de:

- Segurança da Informação
- Administração de Sistemas Linux e Windows
- Redes de Computadores
- Computação Forense
- Pentest
- Hardening
- Virtualização
- Monitoramento
- Documentação Técnica
- Modelagem 3D aplicada à Segurança Física

---

# 🏛️ Arquitetura do Laboratório

O laboratório representa uma empresa fictícia denominada **CyberTécnica LTDA**, organizada em três andares físicos e uma estação dedicada à simulação de ataques.

Cada ambiente possui uma função específica dentro da organização, reproduzindo cenários encontrados em empresas reais.



---

A **Parte 2** trará toda a seção **Etapas Concluídas**, incluindo:

- Ubuntu Server
- Apache
- PHP
- Windows
- Wireshark
- Kali Linux
- **UFW (Firewall)**
- **Hardening**
- **Aprendizados**
- Nmap
- VeraCrypt
- Computação Forense

Essa será a parte mais técnica do README.

---

# 📚 Documentação e Portfólio

Todo o desenvolvimento do laboratório foi documentado para garantir rastreabilidade, reprodutibilidade e organização das atividades.

## ✅ Documentação produzida

- [x] Repositório GitHub estruturado
- [x] README profissional
- [x] Checklist de evolução do projeto
- [x] Documentação técnica em Markdown
- [x] Capturas de tela organizadas
- [x] Projeto publicado no GitHub Pages
- [x] Logomarca desenvolvida em Python utilizando Pillow
- [x] Procedimentos forenses documentados
- [x] Walkthrough completo do laboratório

---

# 📸 Galeria de Evidências

Durante o desenvolvimento foram registradas diversas evidências das atividades realizadas.

As principais capturas encontram-se na pasta:

```
screenshots/
```

Entre elas:

- Instalação das máquinas virtuais
- Configuração das redes
- Apache em funcionamento
- Formulário corporativo
- Capturas do Wireshark
- Escaneamentos realizados com Nmap
- Configuração do Firewall
- VeraCrypt
- Preservação forense
- Estrutura do laboratório

Também é possível visualizar todas as evidências através do GitHub Pages do projeto.

---

# 🛠️ Ferramentas e Tecnologias

| Categoria | Tecnologias |
|------------|-------------|
| **Virtualização** | VirtualBox 7.2.8, Guest Additions |
| **Sistemas Operacionais** | Ubuntu Server, Windows 10, Kali Linux |
| **Redes** | Bridge, NAT, ICMP, TCP/IP, SMB, RPC |
| **Firewall** | UFW (Uncomplicated Firewall), Windows Defender Firewall |
| **Serviços** | Apache2, PHP |
| **Análise de Rede** | Wireshark |
| **Pentest** | Nmap |
| **Criptografia** | VeraCrypt (AES-256) |
| **Computação Forense** | dcfldd, MD5, SHA-1 |
| **Documentação** | GitHub, Markdown |
| **Programação** | Python (Pillow) |
| **Modelagem 3D** | FreeCAD *(em desenvolvimento)* |

---

# 📚 Lições Aprendidas

O desenvolvimento do laboratório proporcionou experiência prática em diversas áreas da Segurança da Informação.

Entre os principais conhecimentos consolidados estão:

- Administração de servidores Linux.
- Administração de estações Windows.
- Virtualização utilizando VirtualBox.
- Configuração de redes em modo Bridge.
- Endereçamento IP.
- Captura e análise de tráfego utilizando Wireshark.
- Reconhecimento de hosts e serviços utilizando Nmap.
- Hardening de servidores Linux.
- Configuração de firewalls.
- Preservação forense de dispositivos de armazenamento.
- Criptografia de dados utilizando VeraCrypt.
- Organização de documentação técnica.
- Desenvolvimento de portfólio profissional.

---

## 🔐 Destaque Técnico

Uma das principais práticas implementadas foi a política padrão do **UFW**:

```bash
deny incoming
allow outgoing
```

Essa abordagem segue o princípio do **menor privilégio**, permitindo que o servidor estabeleça conexões de saída normalmente, enquanto bloqueia conexões de entrada não autorizadas.

Essa configuração reduz significativamente a superfície de ataque e representa uma prática recomendada para ambientes corporativos.

---

# 🚀 Próximos Passos

O laboratório continuará evoluindo para representar uma infraestrutura corporativa ainda mais completa.

## 🌐 Redes e Segurança

- [ ] Implantação do pfSense como firewall principal
- [ ] Segmentação da rede utilizando VLANs
- [ ] Implementação de DMZ
- [ ] Isolamento lógico dos três andares
- [ ] Regras avançadas de firewall
- [ ] VPN para acesso remoto seguro

---

## 🛡️ Defesa

- [ ] Implantação do Snort
- [ ] Implantação do Suricata
- [ ] Centralização de logs
- [ ] Monitoramento de eventos
- [ ] Dashboards de segurança

---

## ⚔️ Segurança Ofensiva

- [ ] Implantação do Metasploit Framework
- [ ] Simulações de ataques controlados
- [ ] Enumeração automatizada
- [ ] Exploração de vulnerabilidades em ambiente isolado

---

## 🏢 Infraestrutura Corporativa

- [ ] Active Directory
- [ ] DNS
- [ ] DHCP
- [ ] Compartilhamento de arquivos
- [ ] Servidor de autenticação
- [ ] Controle de usuários

---

## 🧱 Modelagem 3D

Desenvolvimento completo do prédio da CyberTécnica utilizando FreeCAD.

O objetivo é representar visualmente a infraestrutura física da empresa.

### Térreo

- Recepção
- Controle de acesso
- Catracas
- Câmeras
- Sala de espera

### Primeiro Andar

- Infraestrutura
- Sala dos servidores
- Rack principal
- Cabeamento estruturado
- Sala-cofre

### Segundo Andar

- Diretoria
- Sala SCIF
- Sala de reuniões
- Ambiente de documentos sigilosos

Também está prevista a exportação do modelo em formato **IFC**, permitindo interoperabilidade BIM.

---

## 🤖 Automação

- [ ] Painel administrativo da recepção
- [ ] Banco SQLite
- [ ] Login administrativo
- [ ] Scripts Python para automação
- [ ] Geração automática de relatórios
- [ ] Coleta de logs
- [ ] Dashboard do laboratório

---

## 🎥 Demonstração

- [ ] Produção de vídeo demonstrando toda a infraestrutura.
- [ ] Demonstração prática dos ataques e defesas.
- [ ] Tour completo pelo laboratório.

---

# 📈 Roadmap

```text
Infraestrutura
      │
      ▼
Ubuntu Server
      │
      ▼
Apache + PHP
      │
      ▼
Windows 10
      │
      ▼
Wireshark
      │
      ▼
Kali Linux
      │
      ▼
Firewall UFW
      │
      ▼
VeraCrypt
      │
      ▼
pfSense
      │
      ▼
Snort / Suricata
      │
      ▼
Active Directory
      │
      ▼
SOC Corporativo
```

---

# 👤 Autor

## João Solano

Graduado em História.

Pós-graduado em Ética e Filosofia Política.

Graduado em Análise e Desenvolvimento de Sistemas.

Pós-graduando em **Computação Forense e Perícia Digital**.

Criador do **Laboratório CyberTécnica LTDA**, um ambiente corporativo de cibersegurança voltado ao desenvolvimento de competências práticas em infraestrutura, segurança ofensiva, segurança defensiva, computação forense e documentação técnica.

### Contato

**LinkedIn**

https://www.linkedin.com/in/joão-solano-310774138/

**GitHub**

https://github.com/joaosolano

---

# 📖 Documentação Completa

O projeto possui documentação complementar contendo procedimentos detalhados, capturas de tela e guias técnicos.

## Documentos disponíveis

```
docs/
│
├── PROJECT_WALKTHROUGH.md
├── manual_boas_praticas.md
├── cofre_digital.md
```

---

# 📄 Licença

Este projeto é distribuído sob a licença **MIT**.

Consulte o arquivo:

```
LICENSE
```

para mais informações.

---

# ⭐ Considerações Finais

O **CyberTécnica LTDA** é um laboratório em constante evolução, desenvolvido com o objetivo de aproximar teoria e prática por meio da simulação de uma infraestrutura corporativa realista.

Além de servir como ambiente de estudos em cibersegurança, o projeto também funciona como um portfólio técnico, demonstrando competências em administração de sistemas, redes, hardening, computação forense, segurança ofensiva e documentação profissional.

Cada nova funcionalidade implementada representa um novo cenário de aprendizado, tornando o laboratório uma plataforma permanente para experimentação, validação de conceitos e desenvolvimento contínuo.

---

**Última atualização:** Junho de 2026
