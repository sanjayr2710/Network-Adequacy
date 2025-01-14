import time
import unittest
from Pages.LoginPage import LoginPage
from Locators.PEPageLocators import PEPageLocators
from Pages.NetworkAdequacyPage import *
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_NetworkAdequacy(unittest.TestCase):
    def test_NavigateToRosterTrackerNewPage(self):
        login = LoginPage(self.driver)
        NAPage = NetworkAdequacyPage(self.driver)
        login = LoginPage(self.driver)
        login.Login_to_RA()
        HardWait.hard_wait(10)
        WaitAndAssert.assert_and_wait(PEPageLocators.ProviderExplorerPageHeading, 10)
        NAPage.NavigateToNATab()
        HardWait.hard_wait(5)
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.NATabHeading, 10)
        NAPage.ExpandStateDropDownNATab()

        county_elements_to_select = [
            NetworkAdequacyLocators.Walker_county_search,
            NetworkAdequacyLocators.CATOOSA_county_search,
            NetworkAdequacyLocators.BULLOCH_county_search,
            NetworkAdequacyLocators.WHITFIELD_county_search,
            NetworkAdequacyLocators.TROUP_county_search,
            NetworkAdequacyLocators.EFFINGHAM_county_search,
            NetworkAdequacyLocators.FLOYD_county_search,
            NetworkAdequacyLocators.DADE_county_search,
            NetworkAdequacyLocators.GORDON_county_search,
            NetworkAdequacyLocators.CARROLL_county_search,
            NetworkAdequacyLocators.COLUMBIA_county_search,
            NetworkAdequacyLocators.RICHMOND_county_search,
            NetworkAdequacyLocators.TOWNS_county_search,
            NetworkAdequacyLocators.LOWNDES_county_search,
            NetworkAdequacyLocators.BARTOW_county_search,
            NetworkAdequacyLocators.UNION_county_search,
            NetworkAdequacyLocators.DOUGHERTY_county_search,
            NetworkAdequacyLocators.COBB_county_search,
            NetworkAdequacyLocators.WALTON_county_search,
            NetworkAdequacyLocators.JACKSON_county_search,
            NetworkAdequacyLocators.CHATTOOGA_county_search,
            NetworkAdequacyLocators.DEKALB_county_search,
            NetworkAdequacyLocators.NEWTON_county_search,
            NetworkAdequacyLocators.GWINNETT_county_search,
            NetworkAdequacyLocators.GLYNN_county_search,
            NetworkAdequacyLocators.COWETA_county_search,
            NetworkAdequacyLocators.FULTON_county_search,
            NetworkAdequacyLocators.SEMINOLE_county_search,
            NetworkAdequacyLocators.JENKINS_county_search,
            NetworkAdequacyLocators.BURKE_county_search,
            NetworkAdequacyLocators.BRYAN_county_search,
            NetworkAdequacyLocators.PICKENS_county_search,
            NetworkAdequacyLocators.PAULDING_county_search,
            NetworkAdequacyLocators.RABUN_county_search,
            NetworkAdequacyLocators.LIBERTY_county_search,
            NetworkAdequacyLocators.GILMER_county_search,
            NetworkAdequacyLocators.EVANS_county_search,
            NetworkAdequacyLocators.CLARKE_county_search,
            NetworkAdequacyLocators.STEPHENS_county_search,
            NetworkAdequacyLocators.POLK_county_search,
            NetworkAdequacyLocators.EARLY_county_search,
            NetworkAdequacyLocators.TATTNALL_county_search,
            NetworkAdequacyLocators.HART_county_search,
            NetworkAdequacyLocators.ELBERT_county_search,
            NetworkAdequacyLocators.EMANUEL_county_search,
            NetworkAdequacyLocators.WILKINSON_county_search,
            NetworkAdequacyLocators.FANNIN_county_search,
            NetworkAdequacyLocators.GREENE_county_search,
            NetworkAdequacyLocators.FRANKLIN_county_search,
            NetworkAdequacyLocators.HALL_county_search,
            NetworkAdequacyLocators.MURRAY_county_search,
            NetworkAdequacyLocators.JONES_county_search,
            NetworkAdequacyLocators.GLASCOCK_county_search,
            NetworkAdequacyLocators.HOUSTON_county_search,
            NetworkAdequacyLocators.DODGE_county_search,
            NetworkAdequacyLocators.BANKS_county_search,
            NetworkAdequacyLocators.CHEROKEE_county_search,
            NetworkAdequacyLocators.TOOMBS_county_search,
            NetworkAdequacyLocators.SCREVEN_county_search,
            NetworkAdequacyLocators.WARREN_county_search,
            NetworkAdequacyLocators.WASHINGTON_county_search,
            NetworkAdequacyLocators.JEFFERSON_county_search,
            NetworkAdequacyLocators.QUITMAN_county_search,
            NetworkAdequacyLocators.LAURENS_county_search,
            NetworkAdequacyLocators.MONTGOMERY_county_search,
            NetworkAdequacyLocators.MADISON_county_search,
            NetworkAdequacyLocators.DOUGLAS_county_search,
            NetworkAdequacyLocators.BLECKLEY_county_search,
            NetworkAdequacyLocators.GRADY_county_search,
            NetworkAdequacyLocators.MUSCOGEE_county_search,
            NetworkAdequacyLocators.MCDUFFIE_county_search,
            NetworkAdequacyLocators.BIBB_county_search,
            NetworkAdequacyLocators.HANCOCK_county_search,
            NetworkAdequacyLocators.JOHNSON_county_search,
            NetworkAdequacyLocators.BALDWIN_county_search,
            NetworkAdequacyLocators.PUTNAM_county_search,
            NetworkAdequacyLocators.TREUTLEN_county_search,
            NetworkAdequacyLocators.HEARD_county_search,
            NetworkAdequacyLocators.COFFEE_county_search,
            NetworkAdequacyLocators.BRANTLEY_county_search,
            NetworkAdequacyLocators.BACON_county_search,
            NetworkAdequacyLocators.TELFAIR_county_search,
            NetworkAdequacyLocators.MACON_county_search,
            NetworkAdequacyLocators.MORGAN_county_search,
            NetworkAdequacyLocators.TIFT_county_search,
            NetworkAdequacyLocators.UPSON_county_search,
            NetworkAdequacyLocators.WAYNE_county_search,
            NetworkAdequacyLocators.WHEELER_county_search,
            NetworkAdequacyLocators.PIKE_county_search,
            NetworkAdequacyLocators.TAYLOR_county_search,
            NetworkAdequacyLocators.OCONEE_county_search,
            NetworkAdequacyLocators.HABERSHAM_county_search,
            NetworkAdequacyLocators.PULASKI_county_search,
            NetworkAdequacyLocators.CRISP_county_search,
            NetworkAdequacyLocators.MITCHELL_county_search,
            NetworkAdequacyLocators.MILLER_county_search,
            NetworkAdequacyLocators.DECATUR_county_search,
            NetworkAdequacyLocators.DOOLY_county_search,
            NetworkAdequacyLocators.WARE_county_search,
            NetworkAdequacyLocators.COOK_county_search,
            NetworkAdequacyLocators.ROCKDALE_county_search,
            NetworkAdequacyLocators.BAKER_county_search,
            NetworkAdequacyLocators.LONG_county_search,
            NetworkAdequacyLocators.STEWART_county_search,
            NetworkAdequacyLocators.SPALDING_county_search,
            NetworkAdequacyLocators.ATKINSON_county_search,
            NetworkAdequacyLocators.BUTTS_county_search,
            NetworkAdequacyLocators.CANDLER_county_search,
            NetworkAdequacyLocators.HARRIS_county_search,
            NetworkAdequacyLocators.THOMAS_county_search,
            NetworkAdequacyLocators.SCHLEY_county_search,
            NetworkAdequacyLocators.DAWSON_county_search,
            NetworkAdequacyLocators.CLAY_county_search,
            NetworkAdequacyLocators.JASPER_county_search,
            NetworkAdequacyLocators.WORTH_county_search,
            NetworkAdequacyLocators.SUMTER_county_search,
            NetworkAdequacyLocators.TERRELL_county_search,
            NetworkAdequacyLocators.LINCOLN_county_search,
            NetworkAdequacyLocators.LUMPKIN_county_search,
            NetworkAdequacyLocators.JEFFDAVIS_county_search,
            NetworkAdequacyLocators.CLINCH_county_search,
            NetworkAdequacyLocators.CHATTAHOOCHI_county_search,
            NetworkAdequacyLocators.CLAYTON_county_search,
            NetworkAdequacyLocators.WILKES_county_search,
            NetworkAdequacyLocators.CRAWFORD_county_search,
            NetworkAdequacyLocators.TALIAFERRO_county_search,
            NetworkAdequacyLocators.RANDOLPH_county_search,
            NetworkAdequacyLocators.FAYETTE_county_search,
            NetworkAdequacyLocators.BARROW_county_search,
            NetworkAdequacyLocators.TURNER_county_search,
            NetworkAdequacyLocators.CHATHAM_county_search,
            NetworkAdequacyLocators.TALBOT_county_search,
            NetworkAdequacyLocators.WEBSTER_county_search,
            NetworkAdequacyLocators.MERIWETHER_county_search,
            NetworkAdequacyLocators.MCINTOSH_county_search,
            NetworkAdequacyLocators.BENHILL_county_search,
            NetworkAdequacyLocators.BERRIEN_county_search,
            NetworkAdequacyLocators.COLQUITT_county_search,
            NetworkAdequacyLocators.TWIGGS_county_search,
            NetworkAdequacyLocators.BROOKS_county_search,
            NetworkAdequacyLocators.CAMDEN_county_search,
            NetworkAdequacyLocators.PEACH_county_search,
            NetworkAdequacyLocators.IRWIN_county_search,
            NetworkAdequacyLocators.MONROE_county_search,
            NetworkAdequacyLocators.HARALSON_county_search,
            NetworkAdequacyLocators.PIERCE_county_search,
            NetworkAdequacyLocators.WHITE_county_search,
            NetworkAdequacyLocators.OGLETHORPE_county_search,
            NetworkAdequacyLocators.LAMAR_county_search,
            NetworkAdequacyLocators.LEE_county_search,
            NetworkAdequacyLocators.FORSYTH_county_search,
            NetworkAdequacyLocators.HENRY_county_search,
            NetworkAdequacyLocators.WILCOX_county_search,
            NetworkAdequacyLocators.CALHOUN_county_search,
            NetworkAdequacyLocators.APPLING_county_search,
            NetworkAdequacyLocators.LANIER_county_search,
            NetworkAdequacyLocators.MARION_county_search,
            NetworkAdequacyLocators.ECHOLS_county_search,
            NetworkAdequacyLocators.CHARLTON_county_search
        ]

        for element in county_elements_to_select:

            # This will expand State and search county and navigates from L1 to L2 screen
            HardWait.hard_wait(5)
            WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.ShrinkStateDropDown, 10)
            NAPage.ScrollDownL1Page(element)
            HardWait.hard_wait(5)
            NAPage.NavigateToL2PageByClickingOnFoundElement(element)

            # this will find all the elements on L2 screen and expand them
            elements_to_expand = [
                NetworkAdequacyLocators.AIH_dropDown_L2Page,
                NetworkAdequacyLocators.AAI_dropDown_L2Page,
                NetworkAdequacyLocators.CCS_dropDown_L2Page,
                NetworkAdequacyLocators.CSP_dropDown_L2Page,
                NetworkAdequacyLocators.CS_dropDown_L2Page,
                NetworkAdequacyLocators.CCService_dropDown_L2Page,
                NetworkAdequacyLocators.Dtl_dropDown_L2Page,
                NetworkAdequacyLocators.DR_dropDown_L2Page,
                NetworkAdequacyLocators.GSTNLY_dropDown_L2Page,
                NetworkAdequacyLocators.OBGYN_dropDown_L2Page,
                NetworkAdequacyLocators.ID_dropDown_L2Page,
                NetworkAdequacyLocators.IOR_dropDown_L2Page,
                NetworkAdequacyLocators.MGPY_dropDown_L2Page,
                NetworkAdequacyLocators.NPLGY_dropDown_L2Page,
                NetworkAdequacyLocators.NS_dropDown_L2Page,
                NetworkAdequacyLocators.OMS_dropDown_L2Page,
                NetworkAdequacyLocators.OR_dropDown_L2Page,
                NetworkAdequacyLocators.OPTHMLGY_dropDown_L2Page,
                NetworkAdequacyLocators.OCBH_dropDown_L2Page,
                NetworkAdequacyLocators.OIC_dropDown_L2Page,
                NetworkAdequacyLocators.PS_dropDown_L2Page,
                NetworkAdequacyLocators.PCP_dropDown_L2Page,
                NetworkAdequacyLocators.SNF_dropDown_L2Page,
                NetworkAdequacyLocators.ST_dropDown_L2Page,
                NetworkAdequacyLocators.SS_dropDown_L2Page,
                NetworkAdequacyLocators.UG_dropDown_L2Page,
                NetworkAdequacyLocators.VS_DropDown_L2Page
            ]

            elements_to_click_on_checkbox = [
                NetworkAdequacyLocators.AIH_checkbox_L2Page,
                NetworkAdequacyLocators.AAI_checkbox_L2Page,
                NetworkAdequacyLocators.CCS_checkbox_L2Page,
                NetworkAdequacyLocators.CSP_checkbox_L2Page,
                NetworkAdequacyLocators.CS_checkbox_L2Page,
                NetworkAdequacyLocators.CCService_checkbox_L2Page,
                NetworkAdequacyLocators.Dtl_checkbox_L2Page,
                NetworkAdequacyLocators.DR_checkbox_L2Page,
                NetworkAdequacyLocators.GSTNLY_checkbox_L2Page,
                NetworkAdequacyLocators.OBGYN_checkbox_L2Page,
                NetworkAdequacyLocators.ID_checkbox_L2Page,
                NetworkAdequacyLocators.IOR_checkbox_L2Page,
                NetworkAdequacyLocators.MGPY_checkbox_L2Page,
                NetworkAdequacyLocators.NPLGY_checkbox_L2Page,
                NetworkAdequacyLocators.NS_checkbox_L2Page,
                NetworkAdequacyLocators.OMS_checkbox_L2Page,
                NetworkAdequacyLocators.OR_checkbox_L2Page,
                NetworkAdequacyLocators.OPTHMLGY_checkbox_L2Page,
                NetworkAdequacyLocators.OCBH_checkbox_L2Page,
                NetworkAdequacyLocators.OIC_checkbox_L2Page,
                NetworkAdequacyLocators.PS_checkbox_L2Page,
                NetworkAdequacyLocators.PCP_checkbox_L2Page,
                NetworkAdequacyLocators.SNF_checkbox_L2Page,
                NetworkAdequacyLocators.ST_checkbox_L2Page,
                NetworkAdequacyLocators.SS_checkbox_L2Page,
                NetworkAdequacyLocators.UG_checkbox_L2Page,
                NetworkAdequacyLocators.VS_checkbox_L2Page
            ]

            for elements_expand, elements_checkbox in zip(elements_to_expand, elements_to_click_on_checkbox):
                HardWait.hard_wait(2)
                WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.SpecialtyHeaderL2Page, 10)
                NAPage.ScrollDownAndExpandAllDropDown_L2Page(elements_expand)
                NAPage.ClickOnViewAssociatedProvidersBtn(elements_checkbox)

            elements_only_checkbox = [
                NetworkAdequacyLocators.CARDlGY_checkbox_L2Page,
                NetworkAdequacyLocators.CPT_checkbox_L2Page,
                NetworkAdequacyLocators.DRTMGLY_checkbox_L2Page,
                NetworkAdequacyLocators.EM_checkbox_L2Page,
                NetworkAdequacyLocators.EDGY_checkbox_L2Page,
                NetworkAdequacyLocators.ENT_checkbox_L2Page,
                NetworkAdequacyLocators.GS_checkbox_L2Page,
                NetworkAdequacyLocators.NULGY_checkbox_L2Page,
                NetworkAdequacyLocators.OT_checkbox_L2Page,
                NetworkAdequacyLocators.OS_checkbox_L2Page,
                NetworkAdequacyLocators.PM_checkbox_L2Page,
                NetworkAdequacyLocators.PT_checkbox_L2Page,
                NetworkAdequacyLocators.POD_checkbox_L2Page,
                NetworkAdequacyLocators.PCA_checkbox_L2Page,
                NetworkAdequacyLocators.PSY_checkbox_L2Page,
                NetworkAdequacyLocators.PULGY_checkbox_L2Page,
                NetworkAdequacyLocators.RHNMTY_checkbox_L2Page,
                NetworkAdequacyLocators.URGY_checkbox_L2Page
            ]

            for elements_Checkbox in elements_only_checkbox:
                HardWait.hard_wait(2)
                WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.SpecialtyHeaderL2Page, 10)
                NAPage.ScrollDownAndClickOnAllCheckBox_L2Page(elements_Checkbox)
                NAPage.ClickOnViewAssociatedProvidersBtn(elements_Checkbox)
                time.sleep(2)

            WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.SBABHeaderL1Page, 10)
            HardWait.hard_wait(10)
            NAPage.NavigateToL1Page()
            HardWait.hard_wait(10)

        # xpath2 = NetworkAdequacyLocators.AIH_checkbox_L2Page
        # HardWait.hard_wait(5)
        # NAPage.ClickOnViewAssociatedProvidersBtn(xpath2)
