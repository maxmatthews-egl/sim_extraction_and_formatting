import pandas as pd

sim_path = r"C:\Users\matthewsm\OneDrive - Enstargroup\ERM Risk Folder\Group\Model Risk Management\Enstar Group Capital Model - Validation\2026\0. Data\Sims\6563\One-Year Total Risk Sims.csv"

df = pd.read_csv(sim_path)

egl_sims = df[df['Entity'] == 'egl_group']
cbre_sims = df[df['Entity'] == 'cbre_group']

egl_sims = egl_sims.pivot( index= 'Sim', columns= 'Risk', values= 'Value')
cbre_sims = cbre_sims.pivot( index= 'Sim', columns= 'Risk', values= 'Value')

egl_sims = egl_sims.reset_index()
cbre_sims = cbre_sims.reset_index()

col_order = [ "Sim", "Total Insurance Risk",
    "Total Market Risk",
    "Total Credit Risk",
    "Total Operational Risk",
    "Total SCR"
]

egl_sims = egl_sims.reindex(columns= col_order)
cbre_sims = cbre_sims.reindex(columns= col_order)

egl_sims = egl_sims.sort_values(by = 'Total SCR')
cbre_sims = cbre_sims.sort_values(by = 'Total SCR')


egl_sims.to_excel(r"./MM_egl_sims.xlsx", index = False)
cbre_sims.to_excel(r"./MM_cbre_sims.xlsx", index = False)