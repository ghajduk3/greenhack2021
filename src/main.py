import pandas as pd


if __name__ == "__main__":
    tbl2_obdelava = pd.read_excel("./data/module2/2020/LP2020_ODP-obdelava T2.xlsx", converters={"PREVZETO_OD_MSO_NAZIV": str})
    tbl5_zbiranje = pd.read_excel("./data/module2/2020/LP2020_ODP-zbiranje_T5.xlsx", converters={"ODDANO_KOMU_MSO": str})
    tbl_additional_odpz = pd.read_excel("./data/module2/2020/LP2020_dodatno.xlsx", sheet_name='ODP-Z', converters={"MS": str})
    tbl_additional_odpp = pd.read_excel("./data/module2/2020/LP2020_dodatno.xlsx", sheet_name='ODP-P', converters={"MS": str})
    # print("tbl2_obdelava = ", list(tbl2_obdelava.columns))
    # print("tbl5_zbiranje = ", list(tbl5_zbiranje.columns))
    # print("tbl_add = ", list(tbl_additional_odpz.columns))
    # print("intersection 2-add", set(tbl_additional_odpz.columns).intersection(set(tbl2_obdelava.columns)))
    # print("intersection 5-add", set(tbl_additional_odpz.columns).intersection(set(tbl5_zbiranje.columns)))
    # "ZBIRALEC_MSO"
    join_tbl5_additional = pd.merge(tbl5_zbiranje, tbl_additional_odpz, on='ID_SUBJEKTA').rename(columns={"MS": "ZBIRALEC_MSO", "SIF_ODPADKA": "SIF_ODPADKA_T5"}).drop(columns=["STAT_REGIJA"])
    join_tbl2_additional = pd.merge(tbl2_obdelava, tbl_additional_odpp, left_on='ID_SUBJEKTI', right_on='ID_SUBJEKTA').rename(columns={"MS": "OBDELAVEC_MSO", "SIF_ODPADKA": "SIF_ODPADKA_T2"}).drop(columns=["STAT_REGIJA", "SIF_AKTIVNOST"])

    join_tbl5 = join_tbl5_additional.groupby(
        by=[
            "ID_SUBJEKTA",
            "SIF_ODPADKA_T5",
            "ODDANO_KOMU",
            "ODDANO_KOMU_MSO",
            "TUJ_PREVZEMNIK",
            "DRZAVA_OBDELAVE_TUJINA",
            "SIF_AKTIVNOST",
            "ODPADNE_SVECE_200203_DA_NE",
            "ID_POROCILA_y",
            "VRSTA_POROCILA",
            "LETO_POROCANJA",
            "ZBIRALEC_MSO"
        ], axis=0, as_index=False, dropna=False)["KOLICINA_ODDANA"].sum()
    join_tbl2 = join_tbl2_additional.groupby(
        by=[
            "ID_POROCILA_x",
            "ID_SUBJEKTI",
            "SIF_ODPADKA_T2",
            "PREVZETO_OD",
            "PREVZETO_OD_MSO_NAZIV",
            "DRZAVA_IZVORA",
            "ODPADNE_SVECE_200203_DA_NE",
            "ID_POROCILA_y",
            "VRSTA_POROCILA",
            "LETO_POROCANJA",
            "OBDELAVEC_MSO"
        ], axis=0, as_index=False, dropna=False)["KOLICINA_PREVZETA"].sum()
    join = pd.merge(
        join_tbl5,
        join_tbl2,
        how="outer",
        left_on=["ODDANO_KOMU_MSO", "ZBIRALEC_MSO", "SIF_ODPADKA_T5"],
        right_on=["OBDELAVEC_MSO", "PREVZETO_OD_MSO_NAZIV", "SIF_ODPADKA_T2"]
    )
    join["DIFF_KOLICINA"] = join["KOLICINA_ODDANA"] - join['KOLICINA_PREVZETA']
    join.to_excel("./data/module2/2020/LP2020_T2T5_joined.xlsx")
