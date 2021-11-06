import pandas as pd


if __name__ == "__main__":
    tbl2_obdelava = pd.read_excel("./data/module2/2020/LP2020_ODP-obdelava T2.xlsx", converters={"PREVZETO_OD_MSO_NAZIV": str})
    tbl4_obdelava = pd.read_excel("./data/module2/2020/LP2020_ODP-obdelava T4.xlsx", converters={"ODDANO_KOMU_MSO": str})
    tbl2_zbiranje = pd.read_excel("./data/module2/2020/LP2020_ODP-zbiranje_T2.xlsx", converters={"ZBRANO_OD_MSO": str})
    tbl5_zbiranje = pd.read_excel("./data/module2/2020/LP2020_ODP-zbiranje_T5.xlsx", converters={"ODDANO_KOMU_MSO": str})

    tbl_additional_odpz = pd.read_excel("./data/module2/2020/LP2020_dodatno.xlsx", sheet_name='ODP-Z', converters={"MS": str})
    tbl_additional_odpp = pd.read_excel("./data/module2/2020/LP2020_dodatno.xlsx", sheet_name='ODP-P', converters={"MS": str})

    tbl2o_augmented = pd.merge(tbl2_obdelava, tbl_additional_odpp, left_on='ID_SUBJEKTI', right_on='ID_SUBJEKTA').rename(columns={"MS": "OBDELAVEC_MSO", "SIF_ODPADKA": "SIF_ODPADKA_T2"}).drop(columns=["STAT_REGIJA", "SIF_AKTIVNOST"])
    tbl4o_augmented = pd.merge(tbl4_obdelava, tbl_additional_odpp, left_on='ID_SUBJEKTA', right_on='ID_SUBJEKTA').rename(columns={"MS": "OBDELAVEC_MSO", "SIF_ODPADKA": "SIF_ODPADKA_T4"}).drop(columns=["STAT_REGIJA", "SIF_AKTIVNOST"])
    tbl2z_augmented = pd.merge(tbl2_zbiranje, tbl_additional_odpz, on='ID_SUBJEKTA').rename(columns={"MS": "ZBIRALEC_MSO", "SIF_ODPADKA": "SIF_ODPADKA_T2"}).drop(columns=["STAT_REGIJA"])
    tbl5z_augmented = pd.merge(tbl5_zbiranje, tbl_additional_odpz, on='ID_SUBJEKTA').rename(columns={"MS": "ZBIRALEC_MSO", "SIF_ODPADKA": "SIF_ODPADKA_T5"}).drop(columns=["STAT_REGIJA"])

    tbl2o_agg = tbl2o_augmented.groupby(
        by=["ID_POROCILA_x", "ID_SUBJEKTI", "SIF_ODPADKA_T2", "PREVZETO_OD", "PREVZETO_OD_MSO_NAZIV", "DRZAVA_IZVORA",
            "ODPADNE_SVECE_200203_DA_NE", "VRSTA_POROCILA", "LETO_POROCANJA", "ID_SUBJEKTA", "OBDELAVEC_MSO"],
        axis=0, as_index=False, dropna=False)["KOLICINA_PREVZETA"].sum()
    tbl2z_agg = tbl2z_augmented.groupby(
        by=['ID_POROCILA_x', 'ID_SUBJEKTA', 'SIF_ODPADKA_T2', 'ZBRANO_OD', 'ZBRANO_OD_MSO',
            'ODPADNE_SVECE_200203_DA_NE', 'VRSTA_POROCILA', 'LETO_POROCANJA', 'ZBIRALEC_MSO'],
        axis=0, as_index=False, dropna=False)["KOLICINA_ZBRANA"].sum()
    tbl4o_agg = tbl4o_augmented.groupby(
        ["ID_POROCILA_x", "ID_SUBJEKTA", "SIF_ODPADKA_T4", "IZ_ODPADKA", "ODDANO_KOMU", "ODDANO_KOMU_MSO",
         "TUJ_PREVZEMNIK", "DRZAVA_OBDELAVE_TUJINA", "ODPADNE_SVECE_200203_DA_NE", "VRSTA_POROCILA", "LETO_POROCANJA", "OBDELAVEC_MSO"],
        axis=0, as_index=False, dropna=False)["KOLICINA_PO_OBDELAVI"].sum()
    tbl5z_agg = tbl5z_augmented.groupby(
        by=["ID_SUBJEKTA", "SIF_ODPADKA_T5", "ODDANO_KOMU", "ODDANO_KOMU_MSO", "TUJ_PREVZEMNIK", "DRZAVA_OBDELAVE_TUJINA", "SIF_AKTIVNOST", "ODPADNE_SVECE_200203_DA_NE", "ID_POROCILA_y", "VRSTA_POROCILA", "LETO_POROCANJA", "ZBIRALEC_MSO"],
        axis=0, as_index=False, dropna=False)["KOLICINA_ODDANA"].sum()

    tbl5z2o_join = pd.merge(
        tbl5z_agg,
        tbl2o_agg,
        how="outer",
        left_on=["ODDANO_KOMU_MSO", "ZBIRALEC_MSO", "SIF_ODPADKA_T5"],
        right_on=["OBDELAVEC_MSO", "PREVZETO_OD_MSO_NAZIV", "SIF_ODPADKA_T2"]
    )
    tbl5z2o_join["DIFF_KOLICINA"] = tbl5z2o_join["KOLICINA_ODDANA"] - tbl5z2o_join['KOLICINA_PREVZETA']
    tbl5z2o_join.to_excel("./data/module2/2020/LP2020_T2oT5z_joined.xlsx", index=False)

    tbl2z5z_join = pd.merge(
        tbl5z_agg,
        tbl2z_agg,
        how="outer",
        left_on=["ODDANO_KOMU_MSO", "ZBIRALEC_MSO", "SIF_ODPADKA_T5"],
        right_on=["ZBIRALEC_MSO", "ZBRANO_OD_MSO", "SIF_ODPADKA_T2"]
    )
    tbl2z5z_join["DIFF_KOLICINA"] = tbl2z5z_join["KOLICINA_ODDANA"] - tbl2z5z_join['KOLICINA_ZBRANA']
    tbl2z5z_join.to_excel("./data/module2/2020/LP2020_T2zT5z_joined.xlsx", index=False)

    tbl4o2o_join = pd.merge(
        tbl4o_agg,
        tbl2o_agg,
        how="outer",
        left_on=["ODDANO_KOMU_MSO", "OBDELAVEC_MSO", "SIF_ODPADKA_T4"],
        right_on=["OBDELAVEC_MSO", "PREVZETO_OD_MSO_NAZIV", "SIF_ODPADKA_T2"]
    )
    tbl4o2o_join["DIFF_KOLICINA"] = tbl4o2o_join["KOLICINA_PO_OBDELAVI"] - tbl4o2o_join['KOLICINA_PREVZETA']
    tbl4o2o_join.to_excel("./data/module2/2020/LP2020_T4oT2o_joined.xlsx", index=False)

    tbl4o2z_join = pd.merge(
        tbl4o_agg,
        tbl2z_agg,
        how="outer",
        left_on=["ODDANO_KOMU_MSO", "OBDELAVEC_MSO", "SIF_ODPADKA_T4"],
        right_on=["ZBIRALEC_MSO", "ZBRANO_OD_MSO", "SIF_ODPADKA_T2"]
    )
    tbl4o2z_join["DIFF_KOLICINA"] = tbl4o2z_join["KOLICINA_PO_OBDELAVI"] - tbl4o2z_join['KOLICINA_ZBRANA']
    tbl4o2z_join.to_excel("./data/module2/2020/LP2020_T4oT2z_joined.xlsx", index=False)
