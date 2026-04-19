param(
    [string]$username
)

# Find user properly
$user = Get-ADUser -Filter "SamAccountName -eq '$username'"

if ($user) {
    Disable-ADAccount -Identity $user.DistinguishedName
    Write-Output "User $username disabled successfully"
} else {
    Write-Output "User not found"
}
