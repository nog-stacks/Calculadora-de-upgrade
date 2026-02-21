# --- Planejamento de Upgrade 2026 ---

# Preços encontrados (Dicionário)
precos_alvo = {
    "Processador (Ryzen 5 5500)": 569.99,
    "Placa de Vídeo (RTX 2060)": 899.00,  
    "Gabinete (Aigo C195M)": 109.00,
    "Fans (Kit Rise Mode)": 60.00
}

def calcular_progresso():
    print("=== MONITOR DE UPGRADE ADS 2026 ===")
    saldo_atual = float(input("Quanto você já guardou em R$ "))
    
    total_necessario = sum(precos_alvo.values())
    faltando = total_necessario - saldo_atual
    
    print("\n--- STATUS DOS COMPONENTES ---")
    for peca, valor in precos_alvo.items():
        if saldo_atual >= valor:
            print(f"[V] {peca}: R$ {valor:.2f} (JÁ PODE COMPRAR!)")
        else:
            print(f"[ ] {peca}: R$ {valor:.2f}")

    print("-" * 35)
    if faltando <= 0:
        print("MUITO BOM! Você já tem grana para o PC todo! Partiu Skyrim no Ultra.")
    else:
        porcentagem = (saldo_atual / total_necessario) * 100
        print(f"Progresso Total: {porcentagem:.1f}%")
        print(f"Faltam apenas R$ {faltando:.2f} para completar o setup.")

if __name__ == "__main__":
    calcular_progresso()