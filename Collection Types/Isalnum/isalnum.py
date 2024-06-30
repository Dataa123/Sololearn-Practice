def alphanumeric(password):
    return password.isalnum()

print(alphanumeric("2m8931Mf2O62iu8ddLmHSIA*p"))
print(alphanumeric("2m8931Mf2O62iu8ddLmHSIAp"))

def alpha(variable):
    return variable.isalpha()

print(alpha("fskjtoamsgipajgkatjusa"))
print(alpha("fskjtoamsgipajgkatj usa"))
print(alpha("g saujn5j1w51nj"))