import numpy as np


class IndexBuilder:

    def __init__(self):
        pass

    def compute(self, image, keyIndex):
        index = []
        np.seterr(divide='ignore', invalid='ignore')
        try:
            if keyIndex == "ATSAVI":
                index = self.ATSAVI(image)

            elif keyIndex == "AFRI1600":
                index = self.AFRI1600(image)

            elif keyIndex == "AFRI2100":
                index = self.AFRI2100(image)

            elif keyIndex == "Alteration":
                index = self.Alteration(image)

            elif keyIndex == "ARI":
                index = self.ARI(image)

            elif keyIndex == "AVI":
                index = self.AVI(image)

            elif keyIndex == "ARVI":
                index = self.ARVI(image)

            elif keyIndex == "ARVI2":
                index = self.ARVI(image)

            elif keyIndex == "BWDRVI":
                index = self.BWDRVI(image)

            elif keyIndex == "BRI":
                index = self.BRI(image)

            elif keyIndex == "CCCI":
                index = self.CCCI(image)

            elif keyIndex == "CARI":
                index = self.CARI(image)

            elif keyIndex == "CARI2":
                index = self.CARI2(image)

            elif keyIndex == "Chlgreen":
                index = self.Chlgreen(image)

            elif keyIndex == "CIgreen":
                index = self.CIgreen(image)

            elif keyIndex == "CIrededge":
                index = self.CIrededge(image)

            elif keyIndex == "Chlred-edge":
                index = self.Chlred_edge(image)

            elif keyIndex == "CVI":
                index = self.CVI(image)

            elif keyIndex == "CI":
                index = self.CI(image)

            elif keyIndex == "CTVI":
                index = self.CTVI(image)

            elif keyIndex == "CRI550":
                index = self.CRI550(image)

            elif keyIndex == "CRI700":
                index = self.CRI700(image)

            elif keyIndex == "Datt1":
                index = self.Datt1(image)

            elif keyIndex == "Datt4":
                index = self.Datt4(image)

            elif keyIndex == "Datt6":
                index = self.Datt6(image)

            elif keyIndex == "D678/500":
                index = self.D678_500(image)

            elif keyIndex == "D800/550":
                index = self.D800_550(image)

            elif keyIndex == "D800/680":
                index = self.D800_680(image)

            elif keyIndex == "GDVI":
                index = self.GDVI(image)

            elif keyIndex == "DVIMSS":
                index = self.DVIMSS(image)

            elif keyIndex == "EVI":
                index = self.EVI(image)

            elif keyIndex == "EVI2":
                index = self.EVI2(image)

            elif keyIndex == "EPI":
                index = self.EPI(image)

            elif keyIndex == "Fe2+":
                index = self.Fe2(image)

            elif keyIndex == "Fe3+":
                index = self.Fe3(image)

            elif keyIndex == "Ferric Oxides":
                index = self.Ferric_Oxides(image)

            elif keyIndex == "Ferrous iron":
                index = self.Ferrous_iron(image)

            elif keyIndex == "Ferrous Silicates":
                index = self.Ferrous_Silicates(image)

            elif keyIndex == "GEMI":
                index = self.GEMI(image)

            elif keyIndex == "GVMI":
                index = self.GVMI(image)

            elif keyIndex == "Gossan":
                index = self.Gossan(image)

            elif keyIndex == "GARI":
                index = self.GARI(image)

            elif keyIndex == "GLI":
                index = self.GLI(image)

            elif keyIndex == "GNDVI":
                index = self.GNDVI(image)

            elif keyIndex == "GOSAVI":
                index = self.GOSAVI(image)

            elif keyIndex == "GSAVI":
                index = self.GSAVI(image)

            elif keyIndex == "GBNDVI":
                index = self.GBNDVI(image)

            elif keyIndex == "GRNDVI":
                index = self.GRNDVI(image)

            elif keyIndex == "H":
                index = self.H(image)

            elif keyIndex == "IVI":
                index = self.IVI(image)

            elif keyIndex == "I":
                index = self.I(image)

            elif keyIndex == "IR550":
                index = self.IR550(image)

            elif keyIndex == "IR700":
                index = self.IR700(image)

            elif keyIndex == "Laterite":
                index = self.Laterite(image)

            elif keyIndex == "LCI":
                index = self.LCI(image)

            elif keyIndex == "LWCI":
                index = self.LWCI(image)

            elif keyIndex == "LogR":
                index = self.LogR(image)

            elif keyIndex == "Maccioni":
                index = self.Maccioni(image)

            elif keyIndex == "MCARI/MTVI2":
                index = self.MCARI_MTVI2(image)

            elif keyIndex == "MCARI/OSAVI":
                index = self.MCARI_OSAVI(image)

            elif keyIndex == "mCRIG":
                index = self.mCRIG(image)

            elif keyIndex == "mCRIRE":
                index = self.mCRIRE(image)

            elif keyIndex == "MVI":
                index = self.MVI(image)

            elif keyIndex == "MGVI":
                index = self.MGVI(image)

            elif keyIndex == "MNSI":
                index = self.MNSI(image)

            elif keyIndex == "MSBI":
                index = self.MSBI(image)

            elif keyIndex == "MYVI":
                index = self.MYVI(image)

            elif keyIndex == "mND680":
                index = self.mND680(image)

            elif keyIndex == "mARI":
                index = self.mARI(image)

            elif keyIndex == "MCARI":
                index = self.MCARI(image)

            elif keyIndex == "MCARI1":
                index = self.MCARI1(image)

            elif keyIndex == "MCARI2":
                index = self.MCARI2(image)

            elif keyIndex == "mNDVI":
                index = self.mNDVI(image)

            elif keyIndex == "mSR":
                index = self.mSR(image)

            elif keyIndex == "MSR670":
                index = self.MSR670(image)

            elif keyIndex == "MSRNir/Red":
                index = self.MSRNir_Red(image)

            elif keyIndex == "MSAVI":
                index = self.MSAVI(image)

            elif keyIndex == "MSAVIhyper":
                index = self.MSAVIhyper(image)

            elif keyIndex == "MTVI1":
                index = self.MTVI1(image)

            elif keyIndex == "MTVI2":
                index = self.MTVI2(image)

            elif keyIndex == "NLI":
                index = self.NLI(image)

            elif keyIndex == "Norm G":
                index = self.Norm_G(image)

            elif keyIndex == "Norm NIR":
                index = self.Norm_NIR(image)

            elif keyIndex == "Norm R":
                index = self.Norm_R(image)

            elif keyIndex == "PPR":
                index = self.PPR(image)

            elif keyIndex == "PVR":
                index = self.PVR(image)

            elif keyIndex == "ND774/677":
                index = self.ND774_677(image)

            elif keyIndex == "GNDVIhyper":
                index = self.GNDVIhyper(image)

            elif keyIndex == "ND782/666":
                index = self.ND782_666(image)

            elif keyIndex == "ND790/670":
                index = self.ND790_670(image)

            elif keyIndex == "ND800/2170":
                index = self.ND800_2170(image)

            elif keyIndex == "PSNDc2":
                index = self.PSNDc2(image)

            elif keyIndex == "PSNDc1":
                index = self.PSNDc1(image)

            elif keyIndex == "GNDVIhyper2":
                index = self.GNDVIhyper2(image)

            elif keyIndex == "PSNDb1":
                index = self.PSNDb1(image)

            elif keyIndex == "PSNDa1":
                index = self.PSNDa1(image)

            elif keyIndex == "ND800/680":
                index = self.ND800_680(image)

            elif keyIndex == "NDII":
                index = self.NDII(image)

            elif keyIndex == "NDII2":
                index = self.NDII2(image)

            elif keyIndex == "NDMI":
                index = self.NDMI(image)

            elif keyIndex == "ND827/668":
                index = self.ND827_668(image)

            elif keyIndex == "ND833/1649":
                index = self.ND833_1649(image)

            elif keyIndex == "ND833/658":
                index = self.ND833_658(image)

            elif keyIndex == "SIWSI":
                index = self.SIWSI(image)

            elif keyIndex == "ND895/675":
                index = self.ND895_675(image)

            elif keyIndex == "NGRDI":
                index = self.NGRDI(image)

            elif keyIndex == "NDVI":
                index = self.NDVI(image)

            elif keyIndex == "BNDVI":
                index = self.BNDVI(image)

            elif keyIndex == "MNDVI":
                index = self.MNDVI(image)

            elif keyIndex == "NDRE":
                index = self.NDRE(image)

            elif keyIndex == "NBR":
                index = self.NBR(image)

            elif keyIndex == "RI":
                index = self.RI(image)

            elif keyIndex == "NDSI":
                index = self.NDSI(image)

            elif keyIndex == "NDVI690-710":
                index = self.NDVI690_710(image)

            elif keyIndex == "NDVIc":
                index = self.NDVIc(image)

            elif keyIndex == "OSAVI":
                index = self.OSAVI(image)

            elif keyIndex == "PNDVI":
                index = self.PNDVI(image)

            elif keyIndex == "PVI":
                index = self.PVI(image)

            elif keyIndex == "RARSa1":
                index = self.RARSa1(image)

            elif keyIndex == "RARSa2":
                index = self.RARSa2(image)

            elif keyIndex == "RARSa3":
                index = self.RARSa3(image)

            elif keyIndex == "RARSa4":
                index = self.RARSa4(image)

            elif keyIndex == "RARSc3":
                index = self.RARSc3(image)

            elif keyIndex == "RARSc4":
                index = self.RARSc4(image)

            elif keyIndex == "RDVI":
                index = self.RDVI(image)

            elif keyIndex == "RDVI2":
                index = self.RDVI2(image)

            elif keyIndex == "Rededge1":
                index = self.Rededge1(image)

            elif keyIndex == "Rededge2":
                index = self.Rededge2(image)

            elif keyIndex == "RBNDVI":
                index = self.RBNDVI(image)

            elif keyIndex == "REIP1":
                index = self.REIP1(image)

            elif keyIndex == "REIP2":
                index = self.REIP2(image)

            elif keyIndex == "REIP3":
                index = self.REIP3(image)

            elif keyIndex == "REP":
                index = self.REP(image)

            elif keyIndex == "RSR":
                index = self.RSR(image)

            elif keyIndex == "Rre":
                index = self.Rre(image)

            elif keyIndex == "SAVImir":
                index = self.SAVImir(image)

            elif keyIndex == "IF":
                index = self.IF(image)

            elif keyIndex == "MSI2":
                index = self.MSI2(image)

            elif keyIndex == "MSI":
                index = self.MSI(image)

            elif keyIndex == "TM5/TM7":
                index = self.TM5_TM7(image)

            elif keyIndex == "SR440/740":
                index = self.SR440_740(image)

            elif keyIndex == "BGI":
                index = self.BGI(image)

            elif keyIndex == "SR520/670":
                index = self.SR520_670(image)

            elif keyIndex == "SR550/670":
                index = self.SR550_670(image)

            elif keyIndex == "DSWI-4":
                index = self.DSWI_4(image)

            elif keyIndex == "SR550/800":
                index = self.SR550_800(image)

            elif keyIndex == "GI":
                index = self.GI(image)

            elif keyIndex == "SR560/658":
                index = self.SR560_658(image)

            elif keyIndex == "SR672/550":
                index = self.SR672_550(image)

            elif keyIndex == "SR672/708":
                index = self.SR672_708(image)

            elif keyIndex == "SR674/553":
                index = self.SR674_553(image)

            elif keyIndex == "SR675/555":
                index = self.SR675_555(image)

            elif keyIndex == "SR675/700":
                index = self.SR675_700(image)

            elif keyIndex == "SR675/705":
                index = self.SR675_705(image)

            elif keyIndex == "SR700":
                index = self.SR700(image)

            elif keyIndex == "SR700/670":
                index = self.SR700_670(image)

            elif keyIndex == "SR710/670":
                index = self.SR710_670(image)

            elif keyIndex == "SR735/710":
                index = self.SR735_710(image)

            elif keyIndex == "SR774/677":
                index = self.SR774_677(image)

            elif keyIndex == "SR800/2170":
                index = self.SR800_2170(image)

            elif keyIndex == "PSSRc2":
                index = self.PSSRc2(image)

            elif keyIndex == "PSSRc1":
                index = self.PSSRc1(image)

            elif keyIndex == "SR800/550":
                index = self.SR800_550(image)

            elif keyIndex == "PSSRb1":
                index = self.PSSRb1(image)

            elif keyIndex == "RVI":
                index = self.RVI(image)

            elif keyIndex == "PSSRa1":
                index = self.PSSRa1(image)

            elif keyIndex == "SR800/680":
                index = self.SR800_680(image)

            elif keyIndex == "SR801/550":
                index = self.SR801_550(image)

            elif keyIndex == "SR801/670":
                index = self.SR801_670(image)

            elif keyIndex == "PBI":
                index = self.PBI(image)

            elif keyIndex == "SR833/1649":
                index = self.SR833_1649(image)

            elif keyIndex == "SR833/658":
                index = self.SR833_658(image)

            elif keyIndex == "Datt2":
                index = self.Datt2(image)

            elif keyIndex == "SR860/550":
                index = self.SR860_550(image)

            elif keyIndex == "SR860/708":
                index = self.SR860_708(image)

            elif keyIndex == "RDI":
                index = self.RDI(image)

            elif keyIndex == "SRMIR/Red":
                index = self.SRMIR_Red(image)

            elif keyIndex == "SRNir/700-715":
                index = self.SRNir_700_715(image)

            elif keyIndex == "GRVI":
                index = self.GRVI(image)

            elif keyIndex == "SRNIR/MIR":
                index = self.SRNIR_MIR(image)

            elif keyIndex == "DVI":
                index = self.DVI(image)

            elif keyIndex == "RRI1":
                index = self.RRI1(image)

            elif keyIndex == "IO":
                index = self.IO(image)

            elif keyIndex == "RGR":
                index = self.RGR(image)

            elif keyIndex == "SRRed/NIR":
                index = self.SRRed_NIR(image)

            elif keyIndex == "SRSWIRI/NIR":
                index = self.SRSWIRI_NIR(image)

            elif keyIndex == "SAVI":
                index = self.SAVI(image)

            elif keyIndex == "SARVI":
                index = self.SARVI(image)

            elif keyIndex == "SARVI2":
                index = self.SARVI2(image)

            elif keyIndex == "SAVI3":
                index = self.SAVI3(image)

            elif keyIndex == "SBL":
                index = self.SBL(image)

            elif keyIndex == "Soil Composition Index":
                index = self.Soil_Composition_Index(image)

            elif keyIndex == "SAVI2":
                index = self.SAVI2(image)

            elif keyIndex == "SLAVI":
                index = self.SLAVI(image)

            elif keyIndex == "SQRT(IR/R)":
                index = self.SQRT(image)

            elif keyIndex == "SIPI1":
                index = self.SIPI1(image)

            elif keyIndex == "SIPI3":
                index = self.SIPI3(image)

            elif keyIndex == "SBI":
                index = self.SBI(image)

            elif keyIndex == "GVIMSS":
                index = self.GVIMSS(image)

            elif keyIndex == "NSIMSS":
                index = self.NSIMSS(image)

            elif keyIndex == "SBIMSS":
                index = self.SBIMSS(image)

            elif keyIndex == "GVI":
                index = self.GVI(image)

            elif keyIndex == "WET":
                index = self.WET(image)

            elif keyIndex == "YVIMSS":
                index = self.YVIMSS(image)

            elif keyIndex == "TCARI/OSAVI":
                index = self.TCARI_OSAVI(image)

            elif keyIndex == "TCARI":
                index = self.TCARI(image)

            elif keyIndex == "TNDVI":
                index = self.TNDVI(image)

            elif keyIndex == "TSAVI":
                index = self.TSAVI(image)

            elif keyIndex == "TVI":
                index = self.TVI(image)

            elif keyIndex == "TCI":
                index = self.TCI(image)

            elif keyIndex == "VI700":
                index = self.VI700(image)

            elif keyIndex == "VARIgreen":
                index = self.VARIgreen(image)

            elif keyIndex == "VARI700":
                index = self.VARI700(image)

            elif keyIndex == "VARIrededge":
                index = self.VARIrededge(image)

            elif keyIndex == "WDVI":
                index = self.WDVI(image)

            elif keyIndex == "WDRVI":
                index = self.WDRVI(image)

        except: # ritorna l'indice vuoto se durante il suo calcolo viene individuata una banda inesistente
            return index

        return index

    def ATSAVI(self, image):
        numerator = (image.get_band(7).get_band() - 1.22 * image.get_band(3).get_band() - 0.03)
        denominator = 1.22 * image.get_band(7).get_band() + image.get_band(3).get_band() - 1.22 * 0.03 + 0.08 * (
                1.0 + np.power(1.22, 2.0))
        index = 1.22 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def AFRI1600(self, image):
        numerator = image.get_band(12).get_band()
        denominator = (image.get_band(7).get_band() + 0.66 * image.get_band(12).get_band())
        index = image.get_band(7).get_band() - 0.66 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def AFRI2100(self, image):
        numerator = image.get_band(12).get_band()
        denominator = (image.get_band(7).get_band() + 0.56 * image.get_band(12).get_band())
        index = image.get_band(7).get_band() - 0.5 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def Alteration(self, image):
        numerator = image.get_band(11).get_band()
        denominator = image.get_band(12).get_band()
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ARI(self, image):
        numerator1_1 = 1.0
        denominator1_1 = image.get_band(2).get_band()
        numerator1_2 = 1.0
        denominator1_2 = image.get_band(4).get_band()

        index = np.where(denominator1_1 == 0, 0, numerator1_1 / denominator1_1) - np.where(denominator1_2 == 0, 0,
                                                                                           numerator1_2 / denominator1_2)
        return index

    def AVI(self, image):
        index = 2.0 * image.get_band(9).get_band() - image.get_band(3).get_band()
        return index

    def ARVI(self, image):
        y = 0.069
        numerator = (image.get_band(8).get_band() - image.get_band(3).get_band() - y * (
                image.get_band(3).get_band() - image.get_band(1).get_band()))
        denominator = (image.get_band(8).get_band() + image.get_band(3).get_band() - y * (
                image.get_band(3).get_band() - image.get_band(1).get_band()))
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ARVI2(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = -0.18 + 1.17 * (np.where(denominator == 0, 0, numerator / denominator))
        return index

    def BWDRVI(self, image):
        numerator = (0.1 * image.get_band(7).get_band() - image.get_band(1).get_band())
        denominator = (0.1 * image.get_band(7).get_band() + image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def BRI(self, image):
        numerator1_1 = 1.0
        denominator1_1 = image.get_band(2).get_band()
        numerator1_2 = 1.0
        denominator1_2 = image.get_band(4).get_band()

        numerator2 = np.where(denominator1_1 == 0, 0, numerator1_1 / denominator1_1) - np.where(denominator1_2 == 0, 0,
                                                                                                numerator1_2 / denominator1_2)
        denominator2 = image.get_band(7).get_band()
        index = np.where(denominator2 == 0, 0, numerator2 / denominator2)
        return index

    def CCCI(self, image):
        numerator1 = image.get_band(7).get_band() - image.get_band(4).get_band()
        denominator1 = image.get_band(7).get_band() + image.get_band(4).get_band()
        numerator2 = image.get_band(7).get_band() - image.get_band(3).get_band()
        denominator2 = image.get_band(7).get_band() + image.get_band(3).get_band()
        numerator3 = np.where(denominator1 == 0, 0, numerator1 / denominator1)
        denominator3 = np.where(denominator2 == 0, 0, numerator2 / denominator2)
        index = np.where(denominator3 == 0, 0, numerator3 / denominator3)

        return index

    def CARI(self, image):
        numerator = np.sqrt(np.power((((image.get_band(4).get_band() - image.get_band(
            2).get_band()) / 150.0) * 670.0 + image.get_band(3).get_band() + (image.get_band(2).get_band() - ((
                    (image.get_band(4).get_band() - image.get_band(2).get_band()) / 150.0) * 550.0))), 2.0))
        denominator = np.power(((image.get_band(4).get_band() - image.get_band(2).get_band()) / np.power(150.0, 2.0) + 1.0), 0.5)
        index = np.where(image.get_band(3).get_band() == 0, 0,
                         image.get_band(4).get_band() / image.get_band(3).get_band()) * np.where(denominator == 0, 0,
                                                                                                 numerator / denominator)
        return index

    def CARI2(self, image):
        a = 0.496
        index = (np.absolute((image.get_band(4).get_band() - (image.get_band(2).get_band()) / 150.0 * (
                image.get_band(3).get_band() + (image.get_band(3).get_band() + (
                image.get_band(2).get_band() - (a * (image.get_band(2).get_band()))) / np.power(
            (np.power(a, 2.0) + 1.0), 0.5)))))) * np.where(image.get_band(3).get_band() == 0, 0, image.get_band(4).get_band() / image.get_band(3).get_band())
        return index

    def Chlgreen(self, image):
        index = np.power(image.get_band(2).get_band()==0, 0, np.where(image.get_band(6).get_band() / image.get_band(2).get_band()), (-1.0))
        return index

    def CIgreen(self, image):
        index = np.where(image.get_band(2).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(2).get_band()) - 1.0
        return index

    def CIrededge(self, image):
        index = np.where(image.get_band(4).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(4).get_band()) - 1.0
        return index

    def Chlred_edge(self, image):
        index = np.power(np.where(image.get_band(4).get_band() == 0, 0, (image.get_band(6).get_band() / image.get_band(4).get_band())), (-1.0))
        return index

    def CVI(self, image):
        index = image.get_band(7).get_band() * np.where(np.power(image.get_band(2).get_band(), 2.0) == 0, 0, image.get_band(3).get_band() / np.power(image.get_band(2).get_band(), 2.0))
        return index

    def CI(self, image):
        index = np.where(image.get_band(4).get_band() == 0, 0, (image.get_band(3).get_band() - image.get_band(1).get_band()) / image.get_band(4).get_band())
        return index

    def CTVI(self, image):
        index = ((np.where((image.get_band(3).get_band() + image.get_band(2).get_band()) == 0, 0, (image.get_band(3).get_band() - image.get_band(2).get_band()) / (image.get_band(3).get_band() + image.get_band(2).get_band())) + 0.5) /\
                np.absolute(np.where((image.get_band(3).get_band() + image.get_band(2).get_band()) == 0, 0, (image.get_band(3).get_band() - image.get_band(2).get_band()) / (image.get_band(3).get_band() + image.get_band(2).get_band())) + 0.5)) *\
        np.sqrt(np.absolute((np.where(image.get_band(3).get_band() + image.get_band(2).get_band() == 0, 0, image.get_band(3).get_band() - image.get_band(2).get_band()) / np.where(image.get_band(3).get_band() + image.get_band(2).get_band() == 0, 0, (image.get_band(3).get_band() - image.get_band(2).get_band()) / image.get_band(3).get_band() + image.get_band(2).get_band()))) + 0.5)
        return index

    def CRI550(self, image):
        index = np.power(image.get_band(1).get_band(), (-1.0)) - np.power(image.get_band(3).get_band(), (-1.0))
        return index

    def CRI700(self, image):
        index = np.power(image.get_band(1).get_band(), (-1.0)) - np.power(image.get_band(4).get_band(), (-1.0))
        return index

    def Datt1(self, image):
        index = np.where((image.get_band(7).get_band() - image.get_band(3).get_band()) == 0, 0,
                         (image.get_band(7).get_band() - image.get_band(4).get_band()) / (
                                 image.get_band(7).get_band() - image.get_band(3).get_band()))
        return index

    def Datt4(self, image):
        index = np.where(image.get_band(2).get_band() * image.get_band(4).get_band() == 0, 0, image.get_band(3).get_band() / image.get_band(2).get_band() * image.get_band(4).get_band())
        return index

    def Datt6(self, image):
        index = np.where((image.get_band(2).get_band() * image.get_band(4).get_band()) == 0, 0,image.get_band(8).get_band() / (image.get_band(2).get_band() * image.get_band(4).get_band()))
        return index

    def D678_500(self, image):
        index = np.where(image.get_band(1).get_band() == 0, 0, image.get_band(3).get_band() - image.get_band(1).get_band())
        return index

    def D800_550(self, image):
        index =  np.where(image.get_band(2).get_band() == 0, 0, image.get_band(7).get_band() - image.get_band(2).get_band())
        return index

    def D800_680(self, image):
        index =  np.where(image.get_band(3).get_band() == 0, 0, image.get_band(7).get_band() - image.get_band(3).get_band())
        return index

    def GDVI(self, image):
        index =  np.where(image.get_band(2).get_band() == 0, 0, image.get_band(7).get_band() - image.get_band(2).get_band())
        return index

    def DVIMSS(self, image):
        index = 2.4 * image.get_band(9).get_band() - image.get_band(3).get_band()
        return index

    def EVI(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = ((image.get_band(7).get_band() + 6.0 * image.get_band(3).get_band() - 7.5 * image.get_band(1).get_band()) + 1.0)
        index = 2.5 * np.where(denominator == 0, 0, numerator/denominator)
        return index

    def EVI2(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator =(image.get_band(7).get_band() + image.get_band(3).get_band() + 1.0)
        index = 2.4 * np.where(denominator == 0, 0, numerator/denominator)
        return index

    def EPI(self, image):
        a = 0.331
        b = 0.329
        numerator = image.get_band(3).get_band()
        denominator = np.power((image.get_band(2).get_band() * image.get_band(4).get_band()), b)
        index = a * np.where(denominator == 0, 0, numerator/denominator)
        return index

    def Fe2(self, image):
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(12).get_band() / image.get_band(7).get_band()) + np.where(image.get_band(3).get_band() == 0, 0, image.get_band(
            2).get_band() / image.get_band(3).get_band())
        return index

    def Fe3(self, image):
        index = np.where(image.get_band(2).get_band() == 0, 0, image.get_band(3).get_band() / image.get_band(2).get_band())
        return index

    def Ferric_Oxides(self, image):
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(11).get_band() / image.get_band(7).get_band())
        return index

    def Ferrous_iron(self, image):
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(12).get_band() / image.get_band(7).get_band()) + np.where(image.get_band(3).get_band() == 0, 0, image.get_band(2).get_band() / image.get_band(3).get_band())
        return index

    def Ferrous_Silicates(self, image):
        index = np.where(image.get_band(11).get_band() == 0, 0, image.get_band(12).get_band() / image.get_band(11).get_band())
        return index

    def GEMI(self, image):
        numerator1 = (2.0 * (np.power(image.get_band(7).get_band(), 2.0) - np.power(image.get_band(3).get_band(), 2.0)) + 1.5 * image.get_band(7).get_band() + 0.5 * image.get_band(3).get_band())
        denominator1 = (image.get_band(7).get_band() + image.get_band(3).get_band() + 0.5)
        numerator2 = 1.0 - 0.25 * (2.0 * (np.power(image.get_band(7).get_band(), 2.0) - np.power(image.get_band(3).get_band(), 2.0)) + 1.5 * image.get_band(7).get_band() + 0.5 * image.get_band(3).get_band())
        denominator2 = (image.get_band(7).get_band() + image.get_band(3).get_band() + 0.5)
        numerator3 = image.get_band(3).get_band() - 0.125
        denominator3 = 1.0 - image.get_band(3).get_band()
        index = np.where(denominator1 == 0, 0, numerator1/denominator1) * np.where(denominator2 == 0, 0, numerator2/denominator2) - np.where(denominator3 == 0, 0, numerator3/denominator3)
        return index

    def GVMI(self, image):
        index = ((image.get_band(7).get_band() + 0.1) - (image.get_band(12).get_band() + 0.02)) / (
                (image.get_band(7).get_band() + 0.1) + (image.get_band(12).get_band() + 0.02))
        return index

    def Gossan(self, image):
        index = np.where(image.get_band(3).get_band() == 0, 0, image.get_band(11).get_band() / image.get_band(3).get_band())
        return index

    def GARI(self, image):
        numerator = (image.get_band(7).get_band() - (image.get_band(2).get_band() - (image.get_band(1).get_band() - image.get_band(3).get_band())))
        denominator = (image.get_band(7).get_band() - (image.get_band(2).get_band() + (image.get_band(1).get_band() - image.get_band(3).get_band())))
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GLI(self, image):
        numerator = (2.0 * image.get_band(2).get_band() - image.get_band(3).get_band() - image.get_band(2).get_band())
        denominator = 2.0 * image.get_band(2).get_band() + image.get_band(3).get_band() + image.get_band(1).get_band()
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GNDVI(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(2).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GOSAVI(self, image):
        Y = 0.120
        numerator = (image.get_band(7).get_band() - image.get_band(2).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(2).get_band() + Y)
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GSAVI(self, image):
        L = 0.482
        numerator = (image.get_band(7).get_band() - image.get_band(2).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(2).get_band() + L)
        index = np.where(denominator == 0, 0, numerator / denominator) * (1.0 + L)
        return index

    def GBNDVI(self, image):
        numerator = (image.get_band(7).get_band() - (image.get_band(2).get_band() + image.get_band(1).get_band()))
        denominator = image.get_band(7).get_band() + (image.get_band(2).get_band() + image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GRNDVI(self, image):
        numerator = (image.get_band(7).get_band() - (image.get_band(2).get_band() + image.get_band(3).get_band()))
        denominator = (image.get_band(7).get_band() + (image.get_band(2).get_band() + image.get_band(3).get_band()))
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def H(self, image):
        index = np.arctan((2.0 * image.get_band(3).get_band() - image.get_band(2).get_band() - image.get_band(
            1).get_band()) / 30.5 * (image.get_band(2).get_band() - image.get_band(1).get_band()))
        return index

    def IVI(self, image):
        a = 0.393
        b = 0.809
        index =np.where((a * image.get_band(3).get_band()) == 0, 0, (image.get_band(7).get_band() - b) / (a * image.get_band(3).get_band()))
        return index

    def I(self, image):
        index = (1.0 / (30.5)) * (
                image.get_band(3).get_band() + image.get_band(2).get_band() + image.get_band(1).get_band())
        return index

    def IR550(self, image):
        index = np.power(image.get_band(2).get_band(), (-1.0))
        return index

    def IR700(self, image):
        index = np.power(image.get_band(4).get_band(), (-1.0))
        return index

    def Laterite(self, image):
        index = np.where(image.get_band(12).get_band() == 0, 0, image.get_band(11).get_band() / image.get_band(12).get_band())
        return index

    def LCI(self, image):
        index = np.where(image.get_band(7).get_band() + image.get_band(3).get_band() == 0, 0 ,(image.get_band(7).get_band() - image.get_band(4).get_band()) / (image.get_band(7).get_band() + image.get_band(3).get_band()))
        return index

    def LWCI(self, image):
        MIDIR = 0.101
        index = np.where(-np.log(1.0 - (image.get_band(7).get_band() - MIDIR)) == 0, 0, np.log(1.0 - (image.get_band(7).get_band() - MIDIR)) / (-np.log(1.0 - (image.get_band(7).get_band() - MIDIR))))
        return index

    def LogR(self, image):
        index = np.log(np.where(image.get_band(3).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(3).get_band()))
        return index

    def Maccioni(self, image):
        index = np.where((image.get_band(6).get_band() - image.get_band(3).get_band()) == 0, 0, (image.get_band(6).get_band() - image.get_band(4).get_band()) / (image.get_band(6).get_band() - image.get_band(3).get_band()))
        return index

    def MCARI_MTVI2(self, image):
        numerator2 = 1.2 * (image.get_band(7).get_band() - image.get_band(2).get_band()) - 2.5 * (image.get_band(3).get_band() - image.get_band(2).get_band())
        denominator2 = np.sqrt(np.power((2.0 * image.get_band(7).get_band() + 1.0), 2.0) - (6.0 * image.get_band(7).get_band() - 5.0 * np.sqrt(image.get_band(3).get_band())) - 0.5)
        index = np.where((1.5 * (np.where(denominator2 == 0, 0, numerator2/denominator2))) == 0, 0, (((image.get_band(4).get_band() - image.get_band(3).get_band()) - 0.2 * (
                image.get_band(4).get_band() - image.get_band(2).get_band())) *
                 (np.where(image.get_band(3).get_band() == 0, 0, image.get_band(4).get_band() / image.get_band(3).get_band()))) \
                / (1.5 * (np.where(denominator2 == 0, 0, numerator2/denominator2))))
        return index

    def MCARI_OSAVI(self, image):
        numerator = (image.get_band(4).get_band() - image.get_band(3).get_band()) - 0.2 * (
                image.get_band(4).get_band() - image.get_band(2).get_band()) * np.where(image.get_band(3).get_band()==0, 0, image.get_band(4).get_band() / image.get_band(3).get_band())
        denominator = (1.0 + 0.16) * np.where((image.get_band(7).get_band() + image.get_band(3).get_band() + 0.16) ==0, 0, image.get_band(7).get_band() - image.get_band(3).get_band() / (image.get_band(7).get_band() + image.get_band(3).get_band() + 0.16))
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def mCRIG(self, image):
        index = (np.power(image.get_band(1).get_band(), (-1.0)) - np.power(image.get_band(2).get_band(),
                                                                           (-1.0))) * image.get_band(7).get_band()
        return index

    def mCRIRE(self, image):
        index = (np.power(image.get_band(1).get_band(), (-1.0)) - np.power(image.get_band(4).get_band(),
                                                                           (-1.0))) * image.get_band(7).get_band()
        return index

    def MVI(self, image):
        index = np.where(image.get_band(11).get_band() == 0, 0, image.get_band(9).get_band() / image.get_band(11).get_band())
        return index

    def MGVI(self, image):
        index = -0.386 * image.get_band(2).get_band() - 0.53 * image.get_band(3).get_band() + 0.535 * image.get_band(
            5).get_band() + 0.532 * image.get_band(9).get_band()
        return index

    def MNSI(self, image):
        index = 0.404 * image.get_band(2).get_band() - 0.039 * image.get_band(3).get_band() - 0.505 * image.get_band(
            5).get_band() + 0.762 * image.get_band(9).get_band()
        return index

    def MSBI(self, image):
        index = 0.406 * image.get_band(2).get_band() + 0.6 * image.get_band(3).get_band() + 0.645 * image.get_band(
            5).get_band() + 0.243 * image.get_band(9).get_band()
        return index

    def MYVI(self, image):
        index = 0.723 * image.get_band(2).get_band() - 0.597 * image.get_band(3).get_band() + 0.206 * image.get_band(
            5).get_band() - 0.278 * image.get_band(9).get_band()
        return index

    def mND680(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() - 2.0 * image.get_band(0).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def mARI(self, image):
        index = (np.power(image.get_band(2).get_band(), (-1.0)) - np.power(image.get_band(4).get_band(),
                                                                           (-1.0))) * image.get_band(7).get_band()
        return index

    def MCARI(self, image):
        index = ((image.get_band(4).get_band() - image.get_band(3).get_band()) - 0.2 * (
                image.get_band(4).get_band() - image.get_band(2).get_band())) * np.where(image.get_band(3).get_band() == 0, 0,
                        image.get_band(4).get_band() / image.get_band(3).get_band())
        return index

    def MCARI1(self, image):
        index = 1.2 * (2.5 * (image.get_band(7).get_band() - image.get_band(3).get_band()) - 1.3 * (
                image.get_band(7).get_band() - image.get_band(2).get_band()))
        return index

    def MCARI2(self, image):
        numerator = (2.5 * (image.get_band(7).get_band() - image.get_band(3).get_band()) - 1.3 * (
                image.get_band(7).get_band() - image.get_band(2).get_band()))
        denominator = np.sqrt(np.power((2.0 * image.get_band(7).get_band() + 1.0), 2.0) - (6.0 * image.get_band(7).get_band() - 5.0 * np.sqrt(image.get_band(3).get_band())) - 0.5)
        index = 1.5 *  np.where(denominator == 0, 0, numerator / denominator)
        return index

    def mNDVI(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() - 2.0 * image.get_band(0).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def mSR(self, image):
        index = np.where(image.get_band(3).get_band() - image.get_band(0).get_band() == 0, 0, (image.get_band(7).get_band() - image.get_band(0).get_band()) / (image.get_band(3).get_band() - image.get_band(0).get_band()))
        return index

    def MSR670(self, image):
        index = (image.get_band(7).get_band() / image.get_band(3).get_band() - 1.0) / np.sqrt(
            image.get_band(7).get_band() / image.get_band(3).get_band() + 1.0)
        return index

    def MSRNir_Red(self, image):
        numerator = (np.where(image.get_band(3).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(3).get_band()) - 1.0)
        denominator = np.sqrt(np.where(image.get_band(3).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(3).get_band()) + 1.0)
        index = np.where(denominator == 0, 0, numerator / denominator)

        return index

    def MSAVI(self, image):
        index = (2.0 * image.get_band(7).get_band() + 1.0 - np.sqrt(
            np.power((2.0 * image.get_band(7).get_band() + 1.0), 2.0) - 8.0 * (
                    image.get_band(7).get_band() - image.get_band(3).get_band()))) / 2.0
        return index

    def MSAVIhyper(self, image):
        index = (0.5) * ((2.0 * image.get_band(7).get_band() + 1.0) - np.sqrt(
            np.power((2.0 * image.get_band(7).get_band() + 1.0), 2.0) - 8.0 * (
                    image.get_band(7).get_band() - image.get_band(3).get_band())))
        return index

    def MTVI1(self, image):
        index = 1.2 * (1.2 * (image.get_band(7).get_band() - image.get_band(2).get_band()) - 2.5 * (
                image.get_band(3).get_band() - image.get_band(2).get_band()))
        return index

    def MTVI2(self, image):
        numerator = 1.5 * (1.2 * (image.get_band(7).get_band() - image.get_band(2).get_band()) - 2.5 * (
                image.get_band(3).get_band() - image.get_band(2).get_band()))
        denominator = np.sqrt(
            np.power((2.0 * image.get_band(7).get_band() + 1.0), 2.0) - (
                    6.0 * image.get_band(7).get_band() - 5.0 * np.sqrt(image.get_band(3).get_band())) - 0.5)
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NLI(self, image):
        index = np.where((np.power(image.get_band(7).get_band(), 2.0) + image.get_band(3).get_band())(np.power(image.get_band(7).get_band(), 2.0) + image.get_band(3).get_band()) == 0, 0, (np.power(image.get_band(7).get_band(), 2.0) - image.get_band(3).get_band()) / (np.power(image.get_band(7).get_band(), 2.0) + image.get_band(3).get_band()))
        return index

    def Norm_G(self, image):
        numerator = image.get_band(2).get_band()
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def Norm_NIR(self, image):
        numerator = image.get_band(7).get_band()
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def Norm_R(self, image):
        numerator = image.get_band(3).get_band()
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PPR(self, image):
        numerator = (image.get_band(2).get_band() - image.get_band(0).get_band())
        denominator = (image.get_band(2).get_band() + image.get_band(0).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PVR(self, image):
        numerator = (image.get_band(2).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(2).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND774_677(self, image):
        numerator = (image.get_band(6).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(6).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GNDVIhyper(self, image):
        numerator = (image.get_band(6).get_band() - image.get_band(2).get_band())
        denominator = (image.get_band(6).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND782_666(self, image):
        numerator = (image.get_band(6).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(6).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND790_670(self, image):
        numerator = (image.get_band(6).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(6).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND800_2170(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(12).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(12).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PSNDc2(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(1).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PSNDc1(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(1).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def GNDVIhyper2(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(2).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PSNDb1(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PSNDa1(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND800_680(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDII(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(11).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(11).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDII2(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(11).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(11).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDMI(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(11).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(11).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND827_668(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND833_1649(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(11).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(11).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND833_658(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def SIWSI(self, image):
        numerator = (image.get_band(8).get_band() - image.get_band(11).get_band())
        denominator = (image.get_band(8).get_band() + image.get_band(11).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def ND895_675(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NGRDI(self, image):
        numerator = (image.get_band(2).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(2).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDVI(self, image):
        numerator = (image.get_band(12).get_band() - image.get_band(7).get_band())
        denominator = (image.get_band(12).get_band() + image.get_band(7).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def BNDVI(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(1).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def MNDVI(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(12).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(12).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDRE(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(4).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(4).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NBR(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(12).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(12).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def RI(self, image):
        numerator = (image.get_band(3).get_band() - image.get_band(2).get_band())
        denominator = (image.get_band(3).get_band() + image.get_band(2).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDSI(self, image):
        numerator = (image.get_band(11).get_band() - image.get_band(12).get_band())
        denominator = (image.get_band(11).get_band() + image.get_band(12).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDVI690_710(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(4).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(4).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def NDVIc(self, image):
        SWIRmin = 0.378
        SWIRmax = 0.397
        SWIIRmin = 0.027
        index = np.where((image.get_band(7).get_band() + image.get_band(3).get_band()) == 0, 0, (image.get_band(7).get_band() - image.get_band(3).get_band()) / (image.get_band(7).get_band() + image.get_band(3).get_band())) \
                * (1.0 - (image.get_band(12).get_band() - SWIIRmin) / (SWIRmax - SWIRmin))
        return index

    def OSAVI(self, image):
        index = (1.0 + 0.16) * np.where((image.get_band(7).get_band() + image.get_band(3).get_band() + 0.16) == 0, 0, (image.get_band(7).get_band() - image.get_band(3).get_band()) / (image.get_band(7).get_band() + image.get_band(3).get_band() + 0.16))
        return index

    def PNDVI(self, image):
        numerator = (image.get_band(7).get_band() - (image.get_band(2).get_band() + image.get_band(3).get_band() + image.get_band(1).get_band()))
        denominator = (image.get_band(7).get_band() + (image.get_band(2).get_band() + image.get_band(3).get_band() + image.get_band(1).get_band()))
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def PVI(self, image):
        a = 0.149
        ar = 0.374
        b = 0.735
        index = (1.0 / np.sqrt(np.power(a, 2.0) + 1.0)) * (image.get_band(7).get_band() - ar - b)
        return index

    def RARSa1(self, image):
        r700 = 0.715
        r675 = 0.722
        index = np.where(image.get_band(4).get_band() == 0, 0, image.get_band(3).get_band() / image.get_band(4).get_band()) / (r675 / r700)
        return index

    def RARSa2(self, image):
        r700 = 0.989
        r680 = 0.848
        index = np.where(image.get_band(4).get_band() == 0, 0, image.get_band(3).get_band() / image.get_band(4).get_band()) / (r680 / r700)
        return index

    def RARSa3(self, image):
        r670 = 0.382
        r800 = 0.935
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(3).get_band() / image.get_band(7).get_band()) / (r670 / r800)
        return index

    def RARSa4(self, image):
        r680 = 0.523
        r800 = 0.866
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(3).get_band() / image.get_band(7).get_band()) / (r680 / r800)
        return index

    def RARSc3(self, image):
        r500 = 0.535
        r800 = 0.712
        index = np.where(image.get_band(1).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(1).get_band()) / (r800 / r500)
        return index

    def RARSc4(self, image):
        r470 = 0.503
        r800 = 0.153
        index = np.where(image.get_band(1).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(1).get_band()) / (r800 / r470)
        return index

    def RDVI(self, image):
        denominator = np.power((image.get_band(7).get_band() + image.get_band(3).get_band()), 0.5)
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def RDVI2(self, image):
        denominator = np.sqrt(image.get_band(7).get_band() + image.get_band(3).get_band())
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def Rededge1(self, image):
        index = np.where(image.get_band(3).get_band() == 0, 0, image.get_band(4).get_band() / image.get_band(3).get_band())
        return index

    def Rededge2(self, image):
        index = np.where((image.get_band(4).get_band() + image.get_band(3).get_band()) == 0, 0, (image.get_band(4).get_band() - image.get_band(3).get_band()))
        return index

    def RBNDVI(self, image):
        numerator = (image.get_band(7).get_band() - (image.get_band(3).get_band() + image.get_band(1).get_band()))
        denominator = (image.get_band(7).get_band() + (image.get_band(3).get_band() + image.get_band(1).get_band()))
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def REIP1(self, image):
        numerator = (((image.get_band(3).get_band() + image.get_band(6).get_band()) / 2.0) - image.get_band(
            4).get_band())
        denominator = (image.get_band(5).get_band() - image.get_band(4).get_band())
        index = 700.0 + 40.0 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def REIP2(self, image):
        numerator = (((image.get_band(3).get_band() + image.get_band(6).get_band()) / 2.0) - image.get_band(
            4).get_band())
        denominator = (image.get_band(5).get_band() - image.get_band(4).get_band())
        index = 702.0 + 40.0 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def REIP3(self, image):
        numerator = (((image.get_band(3).get_band() + image.get_band(6).get_band()) / 2.0) - image.get_band(
            4).get_band())
        denominator = (image.get_band(5).get_band() - image.get_band(4).get_band())
        index = 705.0 + 35.0 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def REP(self, image):
        numerator = (((image.get_band(3).get_band() + image.get_band(6).get_band()) / 2.0) - image.get_band(
            4).get_band())
        denominator = (image.get_band(5).get_band() - image.get_band(4).get_band())
        index = 700.0 + 40.0 * np.where(denominator == 0, 0, numerator / denominator)
        return index

    def RSR(self, image):
        MIRmin = 0.259
        MIRmax = 0.640
        index = np.where(image.get_band(3).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(3).get_band()) * MIRmax - image.get_band(
            12).get_band() / MIRmax - MIRmin
        return index

    def Rre(self, image):
        index = (image.get_band(3).get_band() + image.get_band(6).get_band()) / 2.0
        return index

    def SAVImir(self, image):
        L = 0.781
        index = (image.get_band(7).get_band() - image.get_band(12).get_band()) * np.where((image.get_band(7).get_band() + image.get_band(12).get_band() + L) == 0, 0, (1.0 + L) / (image.get_band(7).get_band() + image.get_band(12).get_band() + L))
        return index

    def IF(self, image):
        numerator = 2.0 * image.get_band(3).get_band() - image.get_band(2).get_band() - image.get_band(1).get_band()
        denominator = (image.get_band(2).get_band() - image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator / denominator)
        return index

    def MSI2(self, image):
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(11).get_band() / image.get_band(7).get_band())
        return index

    def MSI(self, image):
        index = np.where(image.get_band(7).get_band() == 0, 0, image.get_band(11).get_band() / image.get_band(7).get_band())
        return index

    def TM5_TM7(self, image):
        index = np.where(image.get_band(12).get_band() == 0, 0, image.get_band(11).get_band() / image.get_band(12).get_band())
        return index

    def SR440_740(self, image):
        index = np.where(image.get_band(5).get_band() == 0, 0, image.get_band(0).get_band() / image.get_band(5).get_band())
        return index

    def BGI(self, image):
        index = np.where(image.get_band(2).get_band()== 0, 0, image.get_band(0).get_band() / image.get_band(2).get_band())
        return index

    def SR520_670(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(1).get_band() / image.get_band(3).get_band())
        return index

    def SR550_670(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(2).get_band() / image.get_band(3).get_band())
        return index

    def DSWI_4(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(2).get_band() / image.get_band(3).get_band())
        return index

    def SR550_800(self, image):
        index = np.where(image.get_band(7).get_band() == 0, image.get_band(2).get_band() / image.get_band(7).get_band())
        return index

    def GI(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(2).get_band() / image.get_band(3).get_band())
        return index

    def SR560_658(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(2).get_band() / image.get_band(3).get_band())
        return index

    def SR672_550(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(3).get_band() / image.get_band(2).get_band())
        return index

    def SR672_708(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(3).get_band() / image.get_band(4).get_band())
        return index

    def SR674_553(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(3).get_band() / image.get_band(2).get_band())
        return index

    def SR675_555(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(3).get_band() / image.get_band(2).get_band())
        return index

    def SR675_700(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(3).get_band() / image.get_band(4).get_band())
        return index

    def SR675_705(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(3).get_band() / image.get_band(4).get_band())
        return index

    def SR700(self, image):
        index = np.where(image.get_band(4).get_band() == 0, 0, 1.0 / image.get_band(4).get_band())
        return index

    def SR700_670(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(4).get_band() / image.get_band(3).get_band())
        return index

    def SR710_670(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(4).get_band() / image.get_band(3).get_band())
        return index

    def SR735_710(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(5).get_band() / image.get_band(4).get_band())
        return index

    def SR774_677(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(6).get_band() / image.get_band(3).get_band())
        return index

    def SR800_2170(self, image):
        index = np.where(image.get_band(12).get_band() == 0, image.get_band(7).get_band() / image.get_band(12).get_band())
        return index

    def PSSRc2(self, image):
        index = np.where(image.get_band(1).get_band() == 0, image.get_band(7).get_band() / image.get_band(1).get_band())
        return index

    def PSSRc1(self, image):
        index = np.where(image.get_band(1).get_band() == 0, image.get_band(7).get_band() / image.get_band(1).get_band())
        return index

    def SR800_550(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(7).get_band() / image.get_band(2).get_band())
        return index

    def PSSRb1(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def RVI(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def PSSRa1(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def SR800_680(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def SR801_550(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(7).get_band() / image.get_band(2).get_band())
        return index

    def SR801_670(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def PBI(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(7).get_band() / image.get_band(2).get_band())
        return index

    def SR833_1649(self, image):
        index = np.where(image.get_band(11).get_band() == 0, image.get_band(7).get_band() / image.get_band(11).get_band())
        return index

    def SR833_658(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def Datt2(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(7).get_band() / image.get_band(4).get_band())
        return index

    def SR860_550(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(8).get_band() / image.get_band(2).get_band())
        return index

    def SR860_708(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(8).get_band() / image.get_band(4).get_band())
        return index

    def RDI(self, image):
        index = np.where(image.get_band(7).get_band() == 0, image.get_band(12).get_band() / image.get_band(7).get_band())
        return index

    def SRMIR_Red(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(12).get_band() / image.get_band(3).get_band())
        return index

    def SRNir_700_715(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(7).get_band() / image.get_band(4).get_band())
        return index

    def GRVI(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(7).get_band() / image.get_band(2).get_band())
        return index

    def SRNIR_MIR(self, image):
        index = np.where(image.get_band(12).get_band() == 0, image.get_band(7).get_band() / image.get_band(12).get_band())
        return index

    def DVI(self, image):
        index = np.where(image.get_band(3).get_band() == 0, image.get_band(7).get_band() / image.get_band(3).get_band())
        return index

    def RRI1(self, image):
        index = np.where(image.get_band(4).get_band() == 0, image.get_band(7).get_band() / image.get_band(4).get_band())
        return index

    def IO(self, image):
        index = np.where(image.get_band(1).get_band() == 0, image.get_band(3).get_band() / image.get_band(1).get_band())
        return index

    def RGR(self, image):
        index = np.where(image.get_band(2).get_band() == 0, image.get_band(3).get_band() / image.get_band(2).get_band())
        return index

    def SRRed_NIR(self, image):
        index = np.where(image.get_band(7).get_band() == 0, image.get_band(3).get_band() / image.get_band(7).get_band())
        return index

    def SRSWIRI_NIR(self, image):
        SWIRI = 0.887
        index = np.where(image.get_band(7).get_band() == 0, 0, SWIRI / image.get_band(7).get_band())
        return index

    def SAVI(self, image):
        L = 0.725
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() + L)
        index = np.where(denominator == 0, 0, numerator/denominator)  * (1.0 + L)
        return index

    def SARVI(self, image):
        y = 0.735
        Rr = 0.740
        L = 0.487
        RB = 0.560
        numerator = (image.get_band(7).get_band() - (Rr - y * (RB - Rr)))
        denominator = (image.get_band(7).get_band() + -(Rr - y * (RB - Rr)) + L)
        index = (1.0 + L) * np.where(denominator == 0, 0, numerator/denominator)
        return index

    def SARVI2(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (1.0 + image.get_band(7).get_band() + 6.0 * image.get_band(3).get_band() - 7.5 * image.get_band(1).get_band())
        index = 2.5 * np.where(denominator == 0, 0, numerator/denominator)
        return index

    def SAVI3(self, image):
        numerator = (image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(7).get_band() + image.get_band(3).get_band() + 0.5)
        index = (1.0 + 0.5) * np.where(denominator == 0, 0, numerator/denominator)
        return index

    def SBL(self, image):
        index = image.get_band(9).get_band() - 2.4 * image.get_band(3).get_band()
        return index

    def Soil_Composition_Index(self, image):
        numerator = (image.get_band(11).get_band() - image.get_band(7).get_band())
        denominator = (image.get_band(11).get_band() + image.get_band(7).get_band())
        index = np.where(denominator == 0, 0, numerator/denominator)
        return index

    def SAVI2(self, image):
        a = 0.064
        b = 0.918
        index = np.where((image.get_band(3).get_band() + b / a) == 0, 0, image.get_band(7).get_band() / (image.get_band(3).get_band() + b / a))
        return index

    def SLAVI(self, image):
        index = np.where((image.get_band(3).get_band() + image.get_band(12).get_band()) == 0, 0, image.get_band(7).get_band() / (image.get_band(3).get_band() + image.get_band(12).get_band()))
        return index

    def SQRT(self, image):
        index = np.sqrt(np.where(image.get_band(3).get_band() == 0, 0, image.get_band(7).get_band() / image.get_band(3).get_band()))
        return index

    def SIPI1(self, image):
        index = np.where((image.get_band(7).get_band() - image.get_band(3).get_band()) == 0, 0, (image.get_band(7).get_band() - image.get_band(0).get_band()) / (image.get_band(7).get_band() - image.get_band(3).get_band()))
        return index

    def SIPI3(self, image):
        index = np.where((image.get_band(7).get_band() - image.get_band(3).get_band()) == 0, 0, (image.get_band(7).get_band() - image.get_band(1).get_band()) / (image.get_band(7).get_band() - image.get_band(3).get_band()))
        return index

    def SBI(self, image):
        index = 0.3037 * image.get_band(1).get_band() + 0.2793 * image.get_band(2).get_band() + 0.4743 * image.get_band(
            3).get_band() + 0.5585 * image.get_band(7).get_band() + 0.5082 * image.get_band(
            10).get_band() + 0.1863 * image.get_band(12).get_band()
        return index

    def GVIMSS(self, image):
        index = -0.283 * image.get_band(2).get_band() - 0.66 * image.get_band(3).get_band() + 0.577 * image.get_band(
            5).get_band() + 0.388 * image.get_band(9).get_band()
        return index

    def NSIMSS(self, image):
        index = -0.016 * image.get_band(2).get_band() + 0.131 * image.get_band(3).get_band() - 0.425 * image.get_band(
            5).get_band() + 0.882 * image.get_band(9).get_band()
        return index

    def SBIMSS(self, image):
        index = 0.332 * image.get_band(2).get_band() + 0.603 * image.get_band(3).get_band() + 0.675 * image.get_band(
            5).get_band() + 0.262 * image.get_band(9).get_band()
        return index

    def GVI(self, image):
        index = -0.2848 * image.get_band(1).get_band() - 0.2435 * image.get_band(
            2).get_band() - 0.5436 * image.get_band(3).get_band() + 0.7243 * image.get_band(
            7).get_band() + 0.084 * image.get_band(11).get_band() - 0.18 * image.get_band(12).get_band()
        return index

    def WET(self, image):
        index = 0.1509 * image.get_band(1).get_band() + 0.1973 * image.get_band(2).get_band() + 0.3279 * image.get_band(
            3).get_band() + 0.3406 * image.get_band(7).get_band() - 0.7112 * image.get_band(
            11).get_band() - 0.4572 * image.get_band(12).get_band()
        return index

    def YVIMSS(self, image):
        index = -0.899 * image.get_band(2).get_band() + 0.428 * image.get_band(3).get_band() + 0.076 * image.get_band(
            5).get_band() - 0.041 * image.get_band(9).get_band()
        return index

    def TCARI_OSAVI(self, image):
        numerator = 3.0 * (image.get_band(4).get_band() - image.get_band(3).get_band()) - 0.2 * (image.get_band(4).get_band() - image.get_band(2).get_band()) * np.where(image.get_band(3).get_band() == 0, 0, image.get_band(4).get_band() / image.get_band(3).get_band())
        denominator = ((1.0 + 0.16) * np.where((image.get_band(7).get_band() + image.get_band(3).get_band() + 0.16) == 0, 0, (image.get_band(7).get_band() - image.get_band(3).get_band()) / (image.get_band(7).get_band() + image.get_band(3).get_band() + 0.16)))
        index = np.where(denominator == 0, 0, numerator/denominator)

        return index

    def TCARI(self, image):
        index = 3.0 * ((image.get_band(4).get_band() - image.get_band(3).get_band()) - 0.2 * (
                image.get_band(4).get_band() - image.get_band(2).get_band()) *
                       np.where(image.get_band(3).get_band() == 0, 0,image.get_band(4).get_band() / image.get_band(3).get_band()))
        return index

    def TNDVI(self, image):
        index = np.sqrt(np.where((image.get_band(7).get_band() + image.get_band(3).get_band()) == 0, 0, (image.get_band(7).get_band() - image.get_band(3).get_band()) / (image.get_band(7).get_band() + image.get_band(3).get_band())) + 0.5)
        return index

    def TSAVI(self, image):
        X = 0.114
        A = 0.824
        B = 0.421
        numerator = (B * (image.get_band(7).get_band() - B * image.get_band(3).get_band() - A))
        denominator = (image.get_band(3).get_band() + B * (image.get_band(7).get_band() - A) + X * (1.0 + np.power(B, 2.0)))
        index = np.where(denominator == 0, 0, numerator/denominator)
        return index

    def TVI(self, image):
        index = np.sqrt((np.where((image.get_band(3).get_band() + image.get_band(2).get_band()) == 0, 0, (image.get_band(3).get_band() - image.get_band(2).get_band()) / (image.get_band(3).get_band() + image.get_band(2).get_band()))) + 0.5)
        return index

    def TCI(self, image):
        index = 1.2 * (image.get_band(4).get_band() - image.get_band(2).get_band()) - 1.5 * (
                image.get_band(3).get_band() - image.get_band(2).get_band()) * np.sqrt(
            np.where(image.get_band(3).get_band() == 0, 0, image.get_band(4).get_band() / image.get_band(3).get_band()))
        return index

    def VI700(self, image):
        index = np.where((image.get_band(4).get_band() + image.get_band(3).get_band()) == 0, 0, (image.get_band(4).get_band() - image.get_band(3).get_band()) / (image.get_band(4).get_band() + image.get_band(3).get_band()))
        return index

    def VARIgreen(self, image):
        numerator = (image.get_band(2).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(2).get_band() + image.get_band(3).get_band() - image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator/denominator)
        return index

    def VARI700(self, image):
        numerator = (image.get_band(4).get_band() - 1.7 * image.get_band(3).get_band() + 0.7 * image.get_band(1).get_band())
        denominator = (image.get_band(4).get_band() + 2.3 * image.get_band(3).get_band() - 1.3 * image.get_band(1).get_band())
        index = np.where(denominator == 0, 0, numerator/denominator)
        return index

    def VARIrededge(self, image):
        numerator = (image.get_band(4).get_band() - image.get_band(3).get_band())
        denominator = (image.get_band(4).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator/denominator)
        return index

    def WDVI(self, image):
        a = 0.752
        index = image.get_band(7).get_band() - a * image.get_band(3).get_band()
        return index

    def WDRVI(self, image):
        numerator = (0.1 * image.get_band(7).get_band() - image.get_band(3).get_band())
        denominator = (0.1 * image.get_band(7).get_band() + image.get_band(3).get_band())
        index = np.where(denominator == 0, 0, numerator/denominator)
        return index
