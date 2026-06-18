#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
from datetime import datetime

def create_backup(source_dir, dest_dir):
    """Cria um backup de logs copiando arquivos .log para a pasta de destino."""
    if not os.path.exists(source_dir):
        print(f"❌ Diretório de origem '{source_dir}' não encontrado.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"📁 Pasta de destino criada: {dest_dir}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(dest_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir)

    copied = 0
    for filename in os.listdir(source_dir):
        if filename.endswith('.log'):
            src_path = os.path.join(source_dir, filename)
            dst_path = os.path.join(backup_dir, filename)
            shutil.copy2(src_path, dst_path)
            print(f"📄 Copiado: {filename}")
            copied += 1

    if copied == 0:
        print("⚠️ Nenhum arquivo .log encontrado.")
        os.rmdir(backup_dir)
    else:
        print(f"\n✅ Backup concluído! {copied} arquivos copiados.")
        print(f"📂 Local: {backup_dir}")

if __name__ == "__main__":
    print("=" * 50)
    print("🔄 Backup de Logs")
    print("=" * 50)

    source = input("📂 Caminho da pasta de logs (ex: /var/log): ").strip()
    if not source:
        print("❌ Caminho vazio. Saindo.")
        sys.exit(1)

    dest = input("📁 Caminho para salvar o backup (ex: ./backups): ").strip()
    if not dest:
        dest = "./backups"

    create_backup(source, dest)
