param(
    [Parameter(Mandatory=$false)]
    [Switch]$clean = $false
)

$scriptDir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
cd $scriptDir
cd ..
rm .\.eggs,.\build,.\dist,.\slashReppo.egg-info,.\slashReppo\__pycache__ -Recurse -Force
echo 'Removed Cached Files'
echo y | pip uninstall slashReppo
echo 'Uninstalled old lib'
if (-not($clean)) {
    python setup.py  sdist bdist_wheel --verbose
    echo 'Built new lib'
    echo y | pip install --find-links=.\dist slashReppo
    echo 'Installed new lib'   
}
