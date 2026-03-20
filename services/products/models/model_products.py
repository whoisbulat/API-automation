from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

class Product(BaseModel):
    """Модель товара"""
    category: str = Field(..., description="Категория товара")
    description: str = Field(..., description="Описание товара")
    id: int = Field(..., description="Уникальный идентификатор")
    image_url: HttpUrl = Field(..., description="URL изображения")
    name: str = Field(..., description="Название товара")
    price: float = Field(..., gt=0, description="Цена товара")
    rating: float = Field(..., ge=0, le=5, description="Рейтинг товара (0-5)")
    reviews_count: int = Field(..., ge=0, description="Количество отзывов")
    stock: int = Field(..., ge=0, description="Остаток на складе")

class Meta(BaseModel):
    """Модель мета-информации пагинации"""
    page: int = Field(..., ge=1, description="Текущая страница")
    per_page: int = Field(..., ge=1, description="Элементов на странице")
    total: int = Field(..., ge=0, description="Всего элементов")
    total_pages: int = Field(..., ge=0, description="Всего страниц")

class ProductResponse(BaseModel):
    """Модель ответа со списком товаров"""
    data: List[Product] = Field(..., description="Список товаров")
    meta: Meta = Field(..., description="Мета-информация о пагинации")