from selenium.webdriver.common.by import By


class LoginLocators:
    EHlogoLogin = (By.XPATH, "//img[@src='/elixir/logo.svg']")
    hilabsLogo = (By.XPATH, "//img[@src='/HiLabs_Primary_RGB.svg']")
    user_id = (By.XPATH, "//input[@class='MuiInputBase-input MuiFilledInput-input MuiInputBase-inputHiddenLabel MuiInputBase-inputAdornedStart css-114cjki']")
    password = (By.XPATH, "//input[@class='MuiInputBase-input MuiFilledInput-input MuiInputBase-inputHiddenLabel MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd css-1i259if']")
    loginButton = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-fullWidth css-1duqoz2']")
    forceLoginPopUp = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1dpu6tj']"
    loginHere = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation css-1t2zyhp']"
