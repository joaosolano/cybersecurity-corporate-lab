#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
from datetime import datetime

def run_nmap_scan(target, options="-sn"):
    """Executa um escaneamento Nmap e retorna a saída."""
    cmd = f"nmap {options} {target}"
    print(f"📡 Executando: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "❌ Escaneamento excedeu o tempo limite (5 min)."
    except Exception as e:
        return f"❌ Erro: {e}"

def save_report(content, filename):
    """Salva o relatório em um arquivo."""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"📄 Relatório salvo em: {filename}")

if __name__ == "__main__":
    print("=" * 50)
    print("🔍 Automatizador de Escaneamento Nmap")
    print("=" * 50)

    target = input("🌐 Digite o alvo (ex: 192.168.18.0/24): ").strip()
    if not target:
        print("❌ Alvo vazio. Saindo.")
        sys.exit(1)

    print("\nOpções de escaneamento:")
    print("1 - Descoberta de rede (-sn)")
    print("2 - Portas comuns (-F)")
    print("3 - Portas específicas (-p 22,80,443)")
    print("4 - Detecção de SO (-O)")
    print("5 - Escaneamento completo (-sS -sV)")

    opcao = input("Escolha uma opção (1-5): ").strip()
    options_map = {
        "1": "-sn",
        "2": "-F",
        "3": "-p 22,80,443",
        "4": "-O",
        "5": "-sS -sV"
    }
    options = options_map.get(opcao, "-sn")
    print(f"\n🔧 Opção selecionada: {options}")

    print("⏳ Escaneando... Aguarde.")
    output = run_nmap_scan(target, options)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_report_{timestamp}.txt"
    save_report(output, filename)

    print("\n✅ Escaneamento concluído!")
    print(f"📋 Resultado disponível em: {filename}")
