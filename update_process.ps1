.\venv\Scripts\activate

# Get the directory of the current script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Define the folder path
$footballDataPath = Join-Path $scriptDir "FootballData"

# Check if "FootballData" exists
if (Test-Path $footballDataPath -PathType Container) {
    # Call Python script inside "FootballData"
    python ./BulkDownload.py
    python ./AnalyseData.py
} else {
    # Call Python script normally
    python ./BulkDownload.py --all
    python ./AnalyseData.py --all
}


