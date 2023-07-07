<#
    GSolone, 2023
    Credits:
        https://stackoverflow.com/a/44337588
    Changes:
        7/7/23- Improve: I provide for download-only capability via script with parameter -DownloadOnly (without installation).
                Change: removed pause command, if I download the installation package I will proceed and notify on screen.
#>

param(
    [Parameter(Mandatory=$False, HelpMessage="Download GoSign Desktop without installing")]
    [switch] $DownloadOnly
)

function downloadMSI($fileURL,$filePath) {
    Invoke-WebRequest -uri $fileURL -OutFile $filePath
    $MSIfile = Get-ChildItem -Path $filePath -File -Filter '*.ms*' 
    Write-Host "MSI found: $($MSIfile)"
    return $MSIfile
}

function installMSI($MSIfile) {
    $checkFile = Test-Path $MSIfile -IsValid
    $today = Get-Date -Format yyyyMMddTHHmmss
    $logFile = '{0}-{1}.log' -f $MSIfile.fullname,$today
    $MSIArguments = @(
        "/i"
        ('"{0}"' -f $MSIfile.fullname)
        "ALLUSERS=1"
        "APPLICATIONFOLDER=`"$env:ProgramFiles\InfoCert\GoSign Desktop`""
        "/quiet"
        "/qn"
        "/norestart"
        "/log"
        $logFile
    )
    
    if ( $checkFile -eq $True ) {
        Write-Host "Installation started: `nmsiexec.exe $($MSIArguments)" -f "Yellow"
        Start-Process "msiexec.exe" -ArgumentList $MSIArguments -Passthru | Wait-Process
        Write-Host "Finished installation $($MSIfile)" -f "Green"
        Remove-Item $MSIfile.fullname -Confirm:$false
    } else {
        Write-Host "File not found." -f "Red"
    }
}

if (!($DownloadOnly)) {
    $MSIfile = downloadMSI "https://rinnovofirma.infocert.it/gosign/download/win32/latest/" "$env:TEMP\GoSign-Desktop-installer-win32.msi"
    installMSI $MSIfile
} else {
    if (!(Test-Path "C:\Temp")) { New-Item "C:\Temp" -ItemType Directory }
    $MSIfile = downloadMSI "https://rinnovofirma.infocert.it/gosign/download/win32/latest/" "C:\Temp\GoSign-Desktop-installer-win32.msi"
}