import pytest
import asyncio
from unittest.mock import AsyncMock, patch
import websockets
from app.main import WebSockets

@pytest.mark.asyncio
async def test_send_data_sends_correctly():

    ws = WebSockets()
    weight = 123.45

    mock_websocket = AsyncMock()
    mock_websocket.send = AsyncMock()

    async def fake_sleep(duration):
        raise asyncio.CancelledError


    with patch("websockets.connect", return_value=AsyncMock(__aenter__=AsyncMock(return_value=mock_websocket),
                                                            __aexit__=AsyncMock(return_value=None))), \
         patch("asyncio.sleep", side_effect=fake_sleep):


        with pytest.raises(asyncio.CancelledError):
            await ws.send_data(weight)


        mock_websocket.send.assert_called_once_with(str(weight))


def test_ws_url_and_interval_defaults():
    ws = WebSockets()
    assert ws.WS_URL == "ws://152.70.50.114:8765/sndr"
    assert ws.SEND_INTERVAL == 2