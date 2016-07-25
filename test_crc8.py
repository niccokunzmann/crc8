"""

This is the definition of the hash function interface from
    https://docs.python.org/2/library/hashlib.html

    The following values are provided as constant attributes of the hash
    objects returned by the constructors:

    hash.digest_size
        The size of the resulting hash in bytes.

    hash.block_size
        The internal block size of the hash algorithm in bytes.

    A hash object has the following methods:

    hash.update(arg)
        Update the hash object with the string arg. Repeated calls are
        equivalent to a single call with the concatenation of all the
        arguments: m.update(a); m.update(b) is equivalent to m.update(a+b).

    hash.digest()
        Return the digest of the strings passed to the update() method so far.
        This is a string of digest_size bytes which may contain non-ASCII
        characters, including null bytes.

    hash.hexdigest()
        Like digest() except the digest is returned as a string of double
        length, containing only hexadecimal digits. This may be used to
        exchange the value safely in email or other non-binary environments.

    hash.copy()
        Return a copy (“clone”) of the hash object. This can be used to
        efficiently compute the digests of strings that share a common
        initial substring.

"""
from crc8 import crc8
import sys
PY2 = sys.version_info[0] == 2

# see this website for example calculation:
#     http://depa.usst.edu.cn/chenjq/www2/software/crc/CRC_Javascript/CRCcalculation.htm
CRC8_INITIAL = b'\x00'
CRC8_INITIAL_HEX = '00'
CRC8_ABC = b'_'
CRC8_ABC_HEX = '5f'
CRC8_123 = b'\xC0'
CRC8_123_HEX = 'c0'


def test_digest_size():
    assert crc8().digest_size == 1


def test_block_size():
    assert crc8().block_size == 1


def test_initial_digest():
    assert crc8().digest() == CRC8_INITIAL


def test_initial_hexdigest():
    assert crc8().hexdigest() == CRC8_INITIAL_HEX


def test_update():
    crc = crc8()
    crc.update(b"abc")
    assert crc.digest() == CRC8_ABC


def test_update123():
    crc = crc8()
    crc.update(b"123")
    assert crc.digest() == CRC8_123
    assert crc.hexdigest() == CRC8_123_HEX


def test_update_split():
    crc = crc8()
    crc.update(b"a")
    crc.update(b"bc")
    assert crc.digest() == CRC8_ABC
    assert crc.hexdigest() == CRC8_ABC_HEX

if PY2:
    try:
        u"\u1234".encode()
    except UnicodeEncodeError as error:
        ENCODE_FAILURE_MESSAGE = error.args[0]
        
    def test_bytes_expected_but_got_string():
        try:
            crc8().update(u"\u1234")
        except UnicodeEncodeError as error:
            assert error.args[0] == ENCODE_FAILURE_MESSAGE
        else:
            assert False, "Can not encode \"\\u1234\"."

    def test_string_accepted():
        crc = crc8()
        crc.update("abc")
        assert crc.digest() == CRC8_ABC
        
else:
    def test_bytes_expected_but_got_string():
        try:
            crc8().update(str())
        except TypeError as e:
            assert e.args[0] == "Unicode-objects must be encoded before hashing"
        else:
            assert False, "Strings can not be passed to crc8 before encoding."


def test_bytes_expected():
    if PY2:
        message = "must be string or buffer"
    else:
        message = "object supporting the buffer API required"
    try:
        crc8().update(None)
    except TypeError as e:
        assert e.args[0] == message
    else:
        assert False, "None can not be passed to crc8 before encoding."


def test_copy():
    crc = crc8()
    crc.update(b'asd')
    crc2 = crc.copy()
    assert crc2 != crc
    assert crc2.digest() == crc.digest()
    crc2.update(b"asd")
    assert crc2.digest() != crc.digest()
    crc.update(b"asd")
    assert crc2.digest() == crc.digest()
    assert crc2.copy() != crc


if __name__ == "__main__":
    import traceback
    failed = 0
    passed = 0
    print("Running tests:")
    print("-" * 40)
    for function_name in dir():
        if function_name.startswith("test_"):
            test_function = globals()[function_name]
            try:
                test_function()
            except:
                
                traceback.print_exc()
                failed += 1
            else:
                print("passed: {0}".format(function_name))
                passed += 1
            print("-" * 40)
    total = failed + passed
    print("=" * 40)
    print("{0} failures; {1} passed; {2} total;".format(failed, passed, total))
