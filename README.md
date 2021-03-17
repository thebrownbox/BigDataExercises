# BigDataExercises

1. To run zeppelin: (Windows PowerShell) </br>
```docker run -p 8080:8080 --rm -v $PWD/logs:/logs -v $PWD/notebook:/notebook -e ZEPPELIN_LOG_DIR='/logs' -e ZEPPELIN_NOTEBOOK_DIR='/notebook' --name zeppelin apache/zeppelin:0.9.0```

<code> Or: Right click file StartZeppelin.ps1, select "Run with Powershell" </code>

2. Access Zeppelin by: localhost:8080