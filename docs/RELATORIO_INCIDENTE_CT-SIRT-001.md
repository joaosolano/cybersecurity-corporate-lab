---
title: Relatório de Incidente CT-SIRT-001/2026
layout: default
permalink: /RELATORIO_INCIDENTE_CT-SIRT-001
---

# 📄 Relatório de Incidente – CT-SIRT-001/2026

## 🔍 Resumo Executivo

| Item | Descrição |
|------|-----------|
| **ID do Incidente** | CT-SIRT-001/2026 |
| **Data** | 19 de junho de 2026 |
| **Sistema Afetado** | VM Kali Linux (Atacante – 192.168.18.31) |
| **Classificação** | Incidente de disponibilidade (nível médio) |
| **Impacto** | Indisponibilidade da VM por aproximadamente 2 horas |
| **Status** | ✅ Resolvido |

---

## 📝 Descrição do Incidente

A VM Kali Linux apresentou falha crítica de boot, entrando em **shell de emergência (initramfs)** com erro relacionado ao driver gráfico `vmwgfx`. O sistema não conseguia carregar a interface gráfica nem completar a inicialização.

### Mensagem de erro observada:
