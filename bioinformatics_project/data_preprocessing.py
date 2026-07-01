import pandas as pd
import numpy as np

def run_data_strategy():
    print("🚀 Updating Preprocessed Data Layer...")
    np.random.seed(42)
    n_samples = 400
    
    sample_ids = [f"GSM{i}" for i in range(100000, 100400)]
    conditions = np.random.choice(["Healthy Control", "Systemic Lupus (SLE)", "Rheumatoid Arthritis (RA)", "Multiple Sclerosis (MS)"], size=n_samples)
    sexes = np.random.choice(["Female", "Male"], size=n_samples, p=[0.80, 0.20])
    ages = np.random.randint(18, 65, size=n_samples)
    
    # Generate continuous clinical lab metric: C-Reactive Protein (CRP) levels in mg/L
    crp_levels = [
        round(np.random.gamma(shape=2, scale=0.5), 2) if c == "Healthy Control" 
        else round(np.random.gamma(shape=5, scale=4), 2) for c in conditions
    ]
    
    clinical_df = pd.DataFrame({
        'Sample_ID': sample_ids, 'Condition': conditions, 'Sex': sexes, 'Age': ages, 'CRP_Levels_mg_L': crp_levels
    })
    
    target_genes = ["STAT1", "IL6", "MX1", "TNF", "IRF7"]
    expression_dict = {'Sample_ID': sample_ids}
    
    for gene in target_genes:
        gene_values = []
        for condition in conditions:
            if condition == "Healthy Control":
                val = np.random.normal(loc=2.2, scale=0.5)
            elif condition == "Systemic Lupus (SLE)" and gene in ["STAT1", "MX1", "IRF7"]:
                val = np.random.normal(loc=8.5, scale=1.1)  # Interferon signature
            elif condition == "Rheumatoid Arthritis (RA)" and gene in ["IL6", "TNF"]:
                val = np.random.normal(loc=7.9, scale=0.9)  # Inflammatory Cytokines
            else:
                val = np.random.normal(loc=4.5, scale=1.2)
            gene_values.append(round(max(0, val), 4))
        expression_dict[gene] = gene_values
        
    expression_df = pd.DataFrame(expression_dict)
    merged_dataset = pd.merge(clinical_df, expression_df, on="Sample_ID")
    merged_dataset.to_csv("autoimmune_processed_data.csv", index=False)
    print("✅ Complete! Ready for the new visualization dashboard.")

if __name__ == "__main__":
    run_data_strategy()