from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class calc(models.Model):
    operation = models.CharField(max_length=200)
    operand1 = models.CharField(max_length=200)
    operand2 = models.CharField(max_length=200)
    
    # operand1 = models.IntegerField()
    # operand2 = models.IntegerField()
    result = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete= models.CASCADE )

    def __str__(self):
        #return self.operand1 + self.operation + self.operand2 + self.result
        return f"UserID {self.user} did operation {self.operation} on operand1 as {self.operand1} and operand2 as {self.operand2} the result of which was {self.result}"

        # return f"UserID {self.user} made this calculation {self.result}"