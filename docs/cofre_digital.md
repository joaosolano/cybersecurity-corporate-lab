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
