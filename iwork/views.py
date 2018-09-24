from django.shortcuts import render
from common.mymako import render_mako_context
from iwork.models import WorkRecord
from common.log import logger

# Create your views here.
def home(request):
    records = WorkRecord.objects.all()
    logger.info("data fetched: {}".format(str(records)))
    return render_mako_context(request, "/iwork/meeting.html", {"operator": "jame", "records": records})