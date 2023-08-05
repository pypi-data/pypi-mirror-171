from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from tom_nonlocalizedevents.tests.factories import SupereventFactory, EventLocalizationFactory


class SupereventAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.superevent1 = SupereventFactory.create(superevent_id='superevent1')
        self.superevent2 = SupereventFactory.create(superevent_id='superevent2')
        self.eventlocalization1 = EventLocalizationFactory.create()
        self.eventlocalization2 = EventLocalizationFactory.create()

        # TODO: sort out django-guardian permissions
        # assign_perm('tom_targets.view_target', self.user, self.st2)

        self.client.force_login(self.user)


class TestSupereventViewSet(SupereventAPITestCase):

    def test_superevent_list_api(self):
        """Test Superevent API list endpoint."""
        response = self.client.get(reverse('api:superevent-list'))

        self.assertEqual(response.json()['count'], 2)
        self.assertContains(response, f'"superevent_id":"{self.superevent1.superevent_id}"')
        self.assertContains(response, f'"superevent_url":"{self.superevent1.superevent_url}"')
        self.assertContains(response, f'"superevent_id":"{self.superevent2.superevent_id}"')
        self.assertContains(response, f'"superevent_url":"{self.superevent2.superevent_url}"')

    def test_superevent_index_view(self):
        response = self.client.get(reverse('nonlocalizedevents:index'))

        self.assertContains(response, self.superevent1.superevent_id)
        self.assertContains(response, self.superevent2.superevent_id)
        self.assertContains(response, reverse('nonlocalizedevents:detail', args=(self.superevent1.pk,)))
        self.assertContains(response, reverse('nonlocalizedevents:detail', args=(self.superevent2.pk,)))

    def test_superevent_detail_view(self):
        response = self.client.get(reverse('nonlocalizedevents:detail', args=(self.superevent1.pk,)))

        self.assertContains(response, self.superevent1.superevent_id)
        self.assertContains(response, "superevent-detail")
        self.assertContains(response, "vue")


class TestEventLocalizationViewSet(SupereventAPITestCase):
    def test_eventlocalization_list(self):
        """Test EventLocalization API list endpoint."""
        response = self.client.get(reverse('api:eventlocalization-list'))

        self.assertEqual(response.json()['count'], 2)
