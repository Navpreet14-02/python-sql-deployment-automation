use EndPointActivity
go

BEGIN TRANSACTION
GO

ALTER TABLE dbo.ActivitySources ADD LastActivityService datetime NULL
GO

SELECT * FROM dbo.ActivitySources
GO

ALTER TABLE dbo.ActivitySources SET (LOCK_ESCALATION = TABLE)
GO

COMMIT