class ClaimsClaims(models.Model):
    brand = models.CharField(db_column='Brand', blank=True, null=True)  # Field name made lowercase.
    application_no = models.CharField(db_column='Application_No', blank=True, null=True)  # Field name made lowercase.
    repair_order_number = models.CharField(db_column='Repair_Order_Number', blank=True, null=True)  # Field name made lowercase.
    repair_claim_garage_code = models.CharField(db_column='Repair_claim_garage_code', blank=True, null=True)  # Field name made lowercase.
    dealerapplicationno = models.CharField(db_column='DealerApplicationNo', blank=True, null=True)  # Field name made lowercase.
    repair_claim_status = models.CharField(db_column='Repair_claim_status', blank=True, null=True)  # Field name made lowercase.
    submission_date = models.TextField(db_column='Submission_date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_review_date = models.TextField(db_column='Repair_claim_review_date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_vehicle_model = models.CharField(db_column='Repair_claim_vehicle_model', blank=True, null=True)  # Field name made lowercase.
    main_damaged_parts_of_repair_claim = models.CharField(db_column='Main_damaged_parts_of_repair_claim', blank=True, null=True)  # Field name made lowercase.
    repair_claim_part_name = models.CharField(db_column='Repair_claim_part_name', blank=True, null=True)  # Field name made lowercase.
    repair_clam_part_qty = models.TextField(db_column='Repair_clam_part_qty', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_application_amount = models.TextField(db_column='Repair_claim_application_amount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_approved_amount = models.TextField(db_column='Repair_claim_approved_amount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_type = models.CharField(db_column='Repair_claim_type', blank=True, null=True)  # Field name made lowercase.
    repair_claim_break_type = models.CharField(db_column='Repair_claim_break_type', blank=True, null=True)  # Field name made lowercase.
    repair_claim_failure_description = models.CharField(db_column='Repair_claim_failure_description', blank=True, null=True)  # Field name made lowercase.
    repair_claim_failure_reson = models.CharField(db_column='Repair_claim_failure_reson', blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', blank=True, null=True)  # Field name made lowercase.
    repair_claim_manufacture_date = models.TextField(db_column='Repair_claim_manufacture_date', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vehicle_purchase_date_of_repair_claim = models.TextField(db_column='Vehicle_purchase_date_of_repair_claim', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_date_of_repair = models.TextField(db_column='Repair_claim_date_of_repair', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_kilometre = models.TextField(db_column='Repair_claim_kilometre', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repair_claim_engine_no = models.CharField(db_column='Repair_claim_engine_no', blank=True, null=True)  # Field name made lowercase.
    repair_claim_transmission_no = models.CharField(db_column='Repair_claim_transmission_no', blank=True, null=True)  # Field name made lowercase.
    cbu_kd = models.CharField(db_column='CBU/KD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    after_sales_customer_files_name = models.CharField(db_column='After_sales_customer_files_name', blank=True, null=True)  # Field name made lowercase.
    repair_claim_claimant = models.CharField(db_column='Repair_claim_claimant', blank=True, null=True)  # Field name made lowercase.
    handler_code = models.CharField(db_column='Handler_code', blank=True, null=True)  # Field name made lowercase.
    repair_claim_comments = models.CharField(db_column='Repair_claim_comments', blank=True, null=True)  # Field name made lowercase.
    repairclaimfailurecode = models.CharField(db_column='RepairClaimFailureCode', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.

    class Meta:
        db_table = 'claims_claims'