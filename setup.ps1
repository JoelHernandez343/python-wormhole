# author: Joel Harim Hernández Javier
# contact: (+52) 55 2175 4478
Param(
    [Parameter(Mandatory = $true)]
    [string]$Command
)

$Global:ProgressPreference = "SilentlyContinue"

$projectName = "git_wormhole"

$executableName = "wormhole"
$initScript = "$executableName.ps1"

$distDir = "dist"
$distPackageName = "$projectName"
$distPackagePath = "$distDir\$distPackageName"
$distFiles = @(
    "src\",
    "__main__.py",
    "__init__.py",
    "README.md",
    "README.html"
)

$scriptsHomeFolder = "python_apps"
$installationPath = "$env:USERPROFILE\$scriptsHomeFolder\$projectName"

function Set-DistPackage {
    # $options = @{
    #     Path             = $distFiles
    #     CompressionLevel = "Optimal"
    #     DestinationPath  = "$distDir\$distZipName"
    # }

    # New-Item -Force $distDir -Type Directory > $null
    # Compress-Archive @options -Force

    Remove-Item -Path $distPackagePath -ErrorAction SilentlyContinue -Force -Recurse
    New-Item -Path $distPackagePath -Type Directory -Force > $null
    Write-Host "> Created $distPackagePath"

    foreach ($file in $distFiles) {
        Copy-Item $file -Destination $distPackagePath -Recurse
    }

    $executableContent = "`$env:PYTHONPATH = `"`$PSScriptRoot;`$env:PYTHONPATH`""
    $executableContent += "`npython -m $projectName `$args"
    $executableContent | Out-File "$distDir\$initScript"

    Write-Host "> Built dist package at $distDir"
}

function Install-Package {
    # build package
    Set-DistPackage

    # environment path
    $currentPath = [System.Environment]::GetEnvironmentVariable("PATH", "User")
    $currentPathValues = $currentPath -split ";"

    if (-not ($currentPathValues -contains $installationPath)) {
        $newPath = "$currentPath;$installationPath"
        [System.Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
        Write-Host "> Added to the user environment: $scriptPath"
    }
    else {
        Write-Host "> The path $installationPath already exists in PATH"
    }

    # set script path
    Remove-Item -Path $installationPath -ErrorAction SilentlyContinue -Force -Recurse
    New-Item -Path $installationPath -Type Directory -Force > $null
    Write-Host "> Created $installationPath"

    # copy dist
    Copy-Item -Path "$distPackagePath" -Destination $installationPath -Recurse
    Write-Host "> Copied $distPackagePath\ to $installationPath"

    # copy dist
    Copy-Item -Path "$distDir\$initScript" -Destination $installationPath
    Write-Host "> Copied $distDir\$initScript to $installationPath"
}

function Uninstall-Package {
    # environment path
    $currentPath = [System.Environment]::GetEnvironmentVariable("PATH", "User")
    $currentPathValues = $currentPath -split ";"

    $newPath = $currentPath -replace "[;]$([regex]::Escape($installationPath))", ""

    if (-not ($currentPathValues -contains $installationPath)) {
        Write-Verbose "> Not in the PATH: $installationPath"
    }
    else {
        [System.Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
        Write-Verbose "> Deleted $installationPath from PATH"
    }

    Remove-Item -Path $installationPath -ErrorAction SilentlyContinue -Force -Recurse
    Write-Host "> Removed $installationPath"
}

if ($Command -eq "dist") {
    Set-DistPackage
}
elseif ($Command -eq "install") {
    Install-Package
}
elseif ($Command -eq "uninstall") {
    Uninstall-Package
}