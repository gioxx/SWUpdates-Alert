<#
    GSolone, 2023
    Credits:
        https://stackoverflow.com/a/44337588
        https://github.com/Squirrel/Squirrel.Windows/issues/1096
    Changes:
        19/10/23- Change: Infocert has seen fit to drop the MSI package for those who download the program for free, repurposing the script to work with the new Squirrel package.
        7/7/23- Improve: I provide for download-only capability via script with parameter -DownloadOnly (without installation).
                Change: removed pause command, if I download the installation package I will proceed and notify on screen.
#>

param(
    [Parameter(Mandatory=$False, HelpMessage="Download GoSign Desktop without installing")]
    [switch] $DownloadOnly
)

function downloadGoSignDesktop($fileURL,$filePath) {
    Invoke-WebRequest -uri $fileURL -OutFile $filePath
    $exeFile = Get-ChildItem -Path $filePath -File -Filter '*.ms*' 
    Write-Host "EXE found: $($exeFile)"
    return $exeFile
}

function installEXE($exeFile) {
    $checkFile = Test-Path $exeFile -IsValid
    $today = Get-Date -Format yyyyMMddTHHmmss
    $logFile = '{0}-{1}.log' -f $exeFile.fullname,$today
    $MSIArguments = @(
        "/i"
        ('"{0}"' -f $exeFile.fullname)
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
        Write-Host "Finished installation $($exeFile)" -f "Green"
        Remove-Item $exeFile.fullname -Confirm:$false
    } else {
        Write-Host "File not found." -f "Red"
    }
}

if (!($DownloadOnly)) {
    $exeFile = downloadGoSignDesktop "https://rinnovofirma.infocert.it/gosign/download/win32/latest/" "$env:TEMP\GoSign-Desktop-installer-win32.exe"
    installEXE $exeFile
} else {
    if (!(Test-Path "C:\Temp")) { New-Item "C:\Temp" -ItemType Directory }
    $exeFile = downloadGoSignDesktop "https://rinnovofirma.infocert.it/gosign/download/win32/latest/" "C:\Temp\GoSign-Desktop-installer-win32.exe"
}