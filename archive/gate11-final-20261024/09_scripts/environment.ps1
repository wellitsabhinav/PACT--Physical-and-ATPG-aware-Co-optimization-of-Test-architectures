param([string]$Script,[string[]]$ScriptArgs=@())
$ErrorActionPreference='Stop'
$gateRoot='F:\Research\PACT\Gate11'
$env:TEMP="$gateRoot\tmp"; $env:TMP=$env:TEMP; $env:TMPDIR=$env:TEMP
$env:PIP_CACHE_DIR="$gateRoot\cache\pip"; $env:XDG_CACHE_HOME="$gateRoot\cache\xdg"; $env:XDG_CONFIG_HOME="$gateRoot\cache\config"
$env:PYTHONPYCACHEPREFIX="$gateRoot\cache\pycache"; $env:PYTHONDONTWRITEBYTECODE='1'; $env:PYTHONNOUSERSITE='1'
$env:MPLCONFIGDIR="$gateRoot\cache\matplotlib"; $env:NUMBA_CACHE_DIR="$gateRoot\cache\numba"; $env:HOME="$gateRoot\cache\home"
$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; $env:PACT_EXPERIMENT_ROOT=$gateRoot
Set-Location -LiteralPath $gateRoot
& 'D:\Python\python.exe' -B $Script @ScriptArgs
exit $LASTEXITCODE
