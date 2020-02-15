# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tennismatch(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=50)  # Field name made lowercase.
    dayofyear = models.DateTimeField(db_column='DayOfYear', blank=True, null=True)  # Field name made lowercase.
    player1id = models.ForeignKey('Tennisplayer', models.DO_NOTHING, db_column='Player1Id')  # Field name made lowercase.
    player2id = models.ForeignKey('Tennisplayer', models.DO_NOTHING, db_column='Player2Id')  # Field name made lowercase.
    event = models.CharField(db_column='Event', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    courttype = models.CharField(db_column='CourtType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tournamentstage = models.CharField(db_column='TournamentStage', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TennisMatch'


class Tennismatchpointbypoint(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    matchid = models.TextField(db_column='MatchId')  # Field name made lowercase.
    stage = models.CharField(db_column='Stage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    playeragames = models.IntegerField(db_column='PlayerAGames')  # Field name made lowercase.
    playerbgames = models.IntegerField(db_column='PlayerBGames')  # Field name made lowercase.
    playerapoint = models.CharField(db_column='PlayerAPoint', max_length=2, blank=True, null=True)  # Field name made lowercase.
    playerbpoint = models.CharField(db_column='PlayerBPoint', max_length=2, blank=True, null=True)  # Field name made lowercase.
    breakpoint = models.BooleanField(db_column='BreakPoint')  # Field name made lowercase.
    setpoint = models.BooleanField(db_column='SetPoint')  # Field name made lowercase.
    matchpoint = models.BooleanField(db_column='MatchPoint')  # Field name made lowercase.
    playeraserving = models.BooleanField(db_column='PlayerAServing')  # Field name made lowercase.
    playerbserving = models.BooleanField(db_column='PlayerBServing')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TennisMatchPointByPoint'


class Tennisplayer(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=50)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TennisPlayer'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'
