from os import path

from src import data


class TestDownload:
    """Test suite for download function from src.data module."""

    def test_download_url(self, requests_mock, tmpdir):
        """Verify the correct endpoint is requested."""
        file_url = "https://www.foo.com/bar.txt"
        requests_mock.get(file_url, text="Tis but a flesh wound!")
        data.download(url=file_url, output_dir=tmpdir.dirname)

        assert requests_mock.last_request.url == file_url
        assert requests_mock.last_request.stream == True

    def test_download_output(self, requests_mock, tmpdir):
        """Verify the downloaded data is saved correctly."""
        file_url = "https://www.foo.com/bar.txt"
        _dir = path.join(tmpdir.dirname, tmpdir.basename)
        requests_mock.get(file_url, text="Tis but a flesh wound!")
        data.download(url=file_url, output_dir=_dir)

        f = tmpdir.join("bar.txt")
        assert f.check()
        assert f.read() == "Tis but a flesh wound!"
