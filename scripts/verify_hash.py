#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import sys
import os

def calculate_hash(file_path, algorithm='md5'):
    """Calcula o hash de um arquivo usando o algoritmo especificado."""
    hash_func = hashlib.md5() if algorithm == 'md5' else hashlib.sha1()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{file_path}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python verify_hash.py <arquivo> [md5|sha1] [hash_esperado]")
        sys.exit(1)

    arquivo = sys.argv[1]
    algoritmo = sys.argv[2] if len(sys.argv) > 2 else 'md5'
    esperado = sys.argv[3] if len(sys.argv) > 3 else None

    if algoritmo not in ['md5', 'sha1']:
        print("❌ Algoritmo inválido. Use 'md5' ou 'sha1'.")
        sys.exit(1)

    calculado = calculate_hash(arquivo, algoritmo)
    print(f"🔐 {algoritmo.upper()}: {calculado}")

    if esperado:
        if calculado == esperado:
            print("✅ OK - Hashes coincidem!")
        else:
            print("❌ FALHA - Hashes NÃO coincidem!")
