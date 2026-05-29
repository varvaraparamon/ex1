import pytest
from decimal import Decimal
from django.contrib.auth.models import User

from catalog.models import Category, Product
from orders.models import Order, OrderItem
from reviews.models import Reviews
from users.models import Profile


@pytest.fixture
def category(db):
    return Category.objects.create(name="Смартфоны", slug="smartphones")


@pytest.fixture
def product(db, category):
    return Product.objects.create(
        category=category,
        title="iPhone 15",
        description="Крутой телефон",
        price=Decimal("99999.99"),
        stock=10,
    )


@pytest.fixture
def user(db):
    return User.objects.create_user(username="alice", password="pass123")


@pytest.fixture
def order(db, user):
    return Order.objects.create(user=user)


@pytest.mark.django_db
class TestCategory:
    def test_str(self, category):
        """Category.__str__ должен возвращать название категории"""
        assert str(category) == "Смартфоны"

    def test_slug_auto_lowercase(self, category):
        assert category.slug == "smartphones"


@pytest.mark.django_db
class TestProduct:
    def test_str(self, product):
        """Product.__str__ содержит название."""
        assert "iPhone 15" in str(product)

    def test_price_positive(self, product):
        assert product.price > 0

    def test_stock_non_negative(self, product):
        assert product.stock >= 0


@pytest.mark.django_db
class TestOrderItem:
    def test_price_snapshot(self, order, product):
        """Цена в OrderItem должна сохраняться как снимок на момент заказа и не меняться, если потом изменилась цена самого товара"""
        item = OrderItem.objects.create(
            order=order,
            product=product,
            price=Decimal("12345.00"),
            quantity=1,
        )
        product.price = Decimal("1.00")
        product.save()
        item.refresh_from_db()
        assert item.price == Decimal("12345.00")

    def test_line_total_calculation(self, order, product):
        item = OrderItem.objects.create(
            order=order,
            product=product,
            price=Decimal("1000.00"),
            quantity=3,
        )
        assert item.price * item.quantity == Decimal("3000.00")


@pytest.mark.django_db
class TestProfileSignals:
    def test_auto_created_on_user_create(self):
        """При создании User должен автоматически создаваться Profile"""
        new_user = User.objects.create_user(username="bob", password="pass")
        assert Profile.objects.filter(user=new_user).exists()

    def test_profile_has_phone_and_address(self, user):
        profile = Profile.objects.get(user=user)
        assert hasattr(profile, 'phone')
        assert hasattr(profile, 'address')


@pytest.mark.django_db
class TestReviews:
    def test_review_str(self, user, product):
        review = Reviews.objects.create(user=user, product=product, text="Класс", rating=5)
        assert review.user == user
        assert review.product == product
        assert review.rating == 5