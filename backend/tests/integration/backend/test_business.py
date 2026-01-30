import uuid
from typing import Any

import pytest
from httpx import AsyncClient


async def create_business(client: AsyncClient) -> Any:
    payload = {
        "name": "Test Business",
        "email": f"{uuid.uuid4()}@example.com",
        "password": "StrongPassword123",
    }

    response = await client.post("/business/create", json=payload)
    assert response.status_code == 201
    return response.json()


@pytest.mark.asyncio
async def test_create_success(client: AsyncClient) -> None:
    payload = {
        "name": "Test Business",
        "email": f"{uuid.uuid4()}@example.com",
        "password": "StrongPassword123",
    }

    response = await client.post("/business/create", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["email"] == payload["email"]
    assert data["name"] == payload["name"]
    assert "id" in data
    assert "status" in data


@pytest.mark.asyncio
async def test_update_success(client: AsyncClient) -> None:
    business = await create_business(client)

    payload = {
        "id": business["id"],
        "name": "Updated Business Name",
    }

    response = await client.patch("/business/update", json=payload)
    assert response.status_code == 202

    data = response.json()
    assert data["id"] == business["id"]
    assert data["name"] == payload["name"]
    assert data["email"] == business["email"]


@pytest.mark.asyncio
async def test_get_by_id_success(client: AsyncClient) -> None:
    business = await create_business(client)

    response = await client.get(f"/business/{business['id']}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == business["id"]
    assert data["email"] == business["email"]
    assert data["name"] == business["name"]
    assert "status" in data


@pytest.mark.asyncio
async def test_get_all_success(
    client: AsyncClient,
) -> None:
    response = await client.get("/business/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_by_email_success(client: AsyncClient) -> None:
    business = await create_business(client)

    payload = {
        "email": business["email"],
    }

    response = await client.post("/business/get_by_email", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == business["id"]
    assert data["email"] == business["email"]
    assert data["name"] == business["name"]


@pytest.mark.asyncio
async def test_delete_success(client: AsyncClient) -> None:
    business = await create_business(client)

    response = await client.request(
        "DELETE",
        "/business/delete",
        json={"id": business["id"]},
    )
    assert response.status_code == 204

    response = await client.get(f"/business/{business['id']}")
    data = response.json()
    assert data["status"] == "suspended"
