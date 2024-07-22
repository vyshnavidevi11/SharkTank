from django.db import models

# Create your models here.
class Dataset(models.Model):
    data_id=models.AutoField(primary_key=True)
    data_set = models.FileField(upload_to='datasetfile')
    gb_accuracy = models.FloatField(null=True)
    gb_precision = models.FloatField(null=True)
    gb_recall = models.FloatField(null=True)
    gb_f1_score = models.FloatField(null=True)
    gb_algo = models.CharField(max_length=500,null=True)
    ad_accuracy = models.FloatField(null=True)
    ad_precision = models.FloatField(null=True)
    ad_recall = models.FloatField(null=True)
    ad_f1_score = models.FloatField(null=True)
    ad_algo = models.CharField(max_length=500,null=True)
    rf_accuracy = models.FloatField(null=True)
    rf_precision = models.FloatField(null=True)
    rf_recall = models.FloatField(null=True)
    rf_f1_score = models.FloatField(null=True)
    rf_algo = models.CharField(max_length=500,null=True)
    class Meta:
        db_table = 'dataset_details'