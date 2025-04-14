def filter_fields(data, fields):

  return {field: data[field] for field in fields if field in   data}
