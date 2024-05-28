from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import apps
from django_apscheduler.jobstores import DjangoJobStore
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
import logging

logger = logging.getLogger(__name__)


def send_newsletter(newsletter_id):
    Newsletter = apps.get_model('newsletter', 'Newsletter')
    Attempt = apps.get_model('newsletter', 'Attempt')
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
        logger.info(f"Sending newsletter {newsletter_id} to clients")
        for client in newsletter.clients.all():
            logger.info(f"Sending email to {client.email}")
            try:
                send_mail(
                    newsletter.message.topic,
                    newsletter.message.content,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[client.email],
                )
                Attempt.objects.create(
                    newsletter=newsletter,
                    client=client,
                    last_attempt_time=timezone.now(),
                    last_attempt_status='S',
                    server_response=200
                )
                logger.info(f"Attempt successful for {client.email}")
            except Exception as e:
                Attempt.objects.create(
                    newsletter=newsletter,
                    client=client,
                    last_attempt_time=timezone.now(),
                    last_attempt_status='F',
                    server_response=500
                )
                logger.error(f"Attempt failed for {client.email}: {e}")
        newsletter.status = 'S'
        newsletter.save()

    except Newsletter.DoesNotExist:
        logger.error(f"Newsletter {newsletter_id} does not exist")
        pass

    except Exception as e:
        newsletter.status = 'F'
        newsletter.save()
        logger.error(f"Error sending newsletter {newsletter_id}: {e}")


def start_scheduler():
    from apscheduler.schedulers.background import BackgroundScheduler
    from django_apscheduler.jobstores import DjangoJobStore

    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.start()
    return scheduler


scheduler = start_scheduler()
