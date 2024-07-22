from django.shortcuts import render,redirect
from django.contrib import messages
from mainapp.models import User
from pickle import load
from django.db.models import Q
from adminapp.models import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score, recall_score, precision_score, auc, roc_auc_score, roc_curve
# Create your views here.
def admin_login(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        if username == "admin" and password == "admin":
            messages.success(req,'Successfully logged in')
            return redirect('index')
        else :
            messages.warning(req,'Incorrect Details')
            return redirect('admin_login')
    return render(req,'main_template/admin-login.html')

def index(req):
    return render(req,'admin_template/index.html')

def pending_users(req):
    users_pending=User.objects.filter(status="pending")
    userpen={"pending":users_pending}
    return render(req,'admin_template/pending-users.html',userpen)

def all_users(req):
    users_all=User.objects.filter(Q(status="accepted")|Q(status="restricted"))
    return render(req,'admin_template/all-users.html',{"alluser":users_all})

def upload_dataset(req):
    if req.method == 'POST':
        dataset = req.FILES['file']
        print(dataset,'dataset')
        data = Dataset.objects.create(data_set=dataset)
        return redirect('view_dataset')
    return render(req,'admin_template/upload-dataset.html')

def view_dataset(req):
    data = Dataset.objects.all().order_by('-data_id').first()
    file = str(data.data_set)
    df = pd.read_csv('./media/'+ file)
    print(df)
    table = df.to_html(table_id='data_table')
    print(table)
    return render(req,'admin_template/view-dataset.html',{'i':data,'t':table})

def gradient_boosting_classifier(req):
    data = Dataset.objects.all().order_by('-data_id').first()
    context={'data':data}
    return render(req,'admin_template/algorithm-gradient-boosting-classifier.html',context)

def ada_boost_classifier(req):
    data = Dataset.objects.all().order_by('-data_id').first()
    context={'data':data}
    return render(req,'admin_template/algorithm-ada-boost-classifier.html',context)

def random_forest_classifier(req):
    data = Dataset.objects.all().order_by('-data_id').first()
    context={'data':data}
    return render(req,'admin_template/algorithm-random-forest-classifier.html',context)



def graph_analasis(req):
    try:
        data = Dataset.objects.all().order_by('-data_id').first()
        gbc_a = data.gb_accuracy*100
        gbc_p = data.gb_precision*100
        gbc_r = data.gb_recall*100
        gbc_f = data.gb_f1_score*100
        rfc_a = data.rf_accuracy*100
        rfc_p = data.rf_precision*100
        rfc_r = data.rf_recall*100
        rfc_f = data.rf_f1_score*100
        ada_a = data.ad_accuracy*100
        ada_p = data.ad_precision*100
        ada_r = data.ad_recall*100
        ada_f = data.ad_f1_score*100
        context = {
            'gbc_a':gbc_a,
            'gbc_p':gbc_p,
            'gbc_r':gbc_r,
            'gbc_f':gbc_f,
            'rfc_a':rfc_a,
            'rfc_p':rfc_p,
            'rfc_r':rfc_r,
            'rfc_f':rfc_f,
            'ada_a':ada_a,
            'ada_p':ada_p,
            'ada_r':ada_r,
            'ada_f':ada_f,
        }
        return render(req,'admin_template/graph-analasis.html',context)
    except:
        messages.warning(req,'Run all 3 algorithms to compare values')
        return redirect('view_dataset')


#button functions

def gbc_runalgo(req,id):
    data = Dataset.objects.get(data_id=id)
    model=load(open('GradientBoostingClassifier.pkl','rb'))
    file = str(data.data_set)
    df_data = pd.read_csv('./media/'+ file,index_col=0)
    X=df_data.drop(['status'],axis=1)
    Y=pd.get_dummies(df_data['status'])
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
    print(x_test.columns,'xxxxxxxxxxxxxxxxxxx')
    prediction=model.predict(x_test)
    Accuracy = accuracy_score(prediction,y_test)
    precision = precision_score(prediction,y_test,average = 'macro')
    recal = recall_score(prediction,y_test,average = 'macro')
    f_score = f1_score(prediction,y_test,average = 'macro')
    print(Accuracy,precision,recal,f_score)
    data.gb_accuracy=Accuracy
    data.gb_precision=precision
    data.gb_recall=recal
    data.gb_f1_score=f_score
    data.gb_algo='gradient_boosting_classifier'
    data.save()
    return redirect('algorithm1')

def ada_runalgo(req,id):
    data = Dataset.objects.get(data_id=id)
    model=load(open('AdaBoostClassifier.pkl','rb'))
    file = str(data.data_set)
    df_data = pd.read_csv('./media/'+ file,index_col=0)
    X=df_data.drop(['status'],axis=1)
    Y=pd.get_dummies(df_data['status'])
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
    prediction=model.predict(x_test)
    Accuracy = accuracy_score(prediction,y_test)
    precision = precision_score(prediction,y_test,average = 'macro')
    recal = recall_score(prediction,y_test,average = 'macro')
    f_score = f1_score(prediction,y_test,average = 'macro')
    print(Accuracy,precision,recal,f_score)
    data.ad_accuracy=Accuracy
    data.ad_precision=precision
    data.ad_recall=recal
    data.ad_f1_score=f_score
    data.ad_algo='ada_boost_classifier'
    data.save()
    return redirect('algorithm2')

def rfc_runalgo(req,id):
    data = Dataset.objects.get(data_id=id)
    model=load(open('RandomForestClassifier.pkl','rb'))
    file = str(data.data_set)
    df_data = pd.read_csv('./media/'+ file,index_col=0)
    X=df_data.drop(['status'],axis=1)
    Y=pd.get_dummies(df_data['status'])
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
    prediction=model.predict(x_test)
    Accuracy = accuracy_score(prediction,y_test)
    precision = precision_score(prediction,y_test,average = 'macro')
    recal = recall_score(prediction,y_test,average = 'macro')
    f_score = f1_score(prediction,y_test,average = 'macro')
    print(Accuracy,precision,recal,f_score)
    data.rf_accuracy=Accuracy
    data.rf_precision=precision
    data.rf_recall=recal
    data.rf_f1_score=f_score
    data.rf_algo='random_forest_classifier'
    data.save()
    return redirect('algorithm3')


def accept(request,id):
    #to get details of specific id
    status_update=User.objects.get(user_id=id)
    #to change the status
    status_update.status = "accepted"
    #saving the details
    status_update.save()
    messages.info(request,'Status has beed accepted')
    return redirect('pending_users')

def reject(request,id):
    status_reject=User.objects.get(user_id=id)
    status_reject.status = "rejected"
    status_reject.save()
    messages.info(request,'Status has beed rejected')
    return redirect('pending_users')

def change_status(request,id):
    status_change=User.objects.get(user_id=id)
    if status_change.status =="accepted" :
        status_change.status = "restricted"
        status_change.save()
        messages.info(request,'Status has beed changed to restricted')
        return redirect('all_users')
    # elif status_change.status =="pending":
    #     status_change.status = "pending"
    #     status_change.save()
    #     return redirect('all_users')
    else:
        status_change.status = "accepted"
        status_change.save()
        messages.info(request,'Status has beed changed to accepted')
        return redirect('all_users')
def remove(request,id):
    status_delete = User.objects.get(user_id=id)
    status_delete.delete()
    messages.warning(request,'User has been removed From database')
    return redirect('all_users')

def admin_logout(request):
    messages.info(request,'You have been logged out!')
    return redirect('admin_login')
